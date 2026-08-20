# SPDX-License-Identifier: GPL-3.0-or-later
"""Single-window GTK3 shell for Schedulae B02."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from schedulae.bibliography import available_tags, available_types, build_delete_impact, duplicate_reference
from schedulae.bibliography_search import CoalescedQueryDispatcher, DEFAULT_BIBLIOGRAPHY_SEARCH_DELAY_MS
from schedulae.gtk_dialogs import (
    ReferenceDraft,
    run_conflict_dialog,
    run_delete_confirmation,
    run_reference_editor,
    show_about,
    show_error,
)
from schedulae.gtk_reference_view import GtkReferenceView
from schedulae.reference_controller import ReferenceController
from schedulae.reference_store import MarkdownReferenceStore, create_empty_reference_library


@dataclass(frozen=True)
class ShellActionState:
    new_reference: bool
    edit_reference: bool
    duplicate_reference: bool
    delete_reference: bool
    search_filters: bool


def compute_action_state(
    *,
    library_open: bool,
    read_only: bool,
    selected: bool,
) -> ShellActionState:
    mutable = bool(library_open and not read_only)
    selected_mutable = bool(mutable and selected)
    return ShellActionState(
        new_reference=mutable,
        edit_reference=selected_mutable,
        duplicate_reference=selected_mutable,
        delete_reference=selected_mutable,
        search_filters=bool(library_open),
    )


def _gtk():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import GLib, Gtk
    return Gtk, GLib


class SchedulaeWindow:
    """One explicit-library window; domain ownership remains in ReferenceController."""

    def __init__(self, application) -> None:
        Gtk, GLib = _gtk()
        self._Gtk = Gtk
        self._GLib = GLib
        self.window = Gtk.ApplicationWindow(application=application)
        self.window.set_title("Schedulae")
        self.window.set_default_size(1020, 680)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect("destroy", self._on_destroy)

        self.controller: ReferenceController | None = None
        self.library_path: str | None = None
        self.view = GtkReferenceView()
        self.view.set_selection_changed(self._on_view_selection_changed)

        self._updating_filters = False
        self._disposed = False
        self._search_dispatcher = CoalescedQueryDispatcher(
            delay_ms=DEFAULT_BIBLIOGRAPHY_SEARCH_DELAY_MS,
            schedule=lambda delay, callback: GLib.timeout_add(delay, callback),
            cancel=lambda source_id: GLib.source_remove(source_id),
            deliver=self._deliver_query,
        )

        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        root.pack_start(self._build_menu_bar(), False, False, 0)
        root.pack_start(self._build_search_row(), False, False, 8)
        root.pack_start(self.view.widget, True, True, 0)
        self.window.add(root)

        self._sync_action_state()

    # ---------- construction ----------
    def _build_menu_bar(self):
        Gtk = self._Gtk
        menu_bar = Gtk.MenuBar()

        file_item = Gtk.MenuItem(label="File")
        file_menu = Gtk.Menu()
        file_item.set_submenu(file_menu)
        new_library = Gtk.MenuItem(label="New Library…")
        new_library.connect("activate", self._new_library_dialog)
        open_library = Gtk.MenuItem(label="Open Library…")
        open_library.connect("activate", self._open_library_dialog)
        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", lambda _item: self.window.close())
        for item in (new_library, open_library, Gtk.SeparatorMenuItem(), quit_item):
            file_menu.append(item)

        ref_item = Gtk.MenuItem(label="Reference")
        ref_menu = Gtk.Menu()
        ref_item.set_submenu(ref_menu)
        self.new_reference_item = Gtk.MenuItem(label="New…")
        self.new_reference_item.connect("activate", self._new_reference)
        self.edit_reference_item = Gtk.MenuItem(label="Edit…")
        self.edit_reference_item.connect("activate", self._edit_reference)
        self.duplicate_reference_item = Gtk.MenuItem(label="Duplicate…")
        self.duplicate_reference_item.connect("activate", self._duplicate_reference)
        self.delete_reference_item = Gtk.MenuItem(label="Delete…")
        self.delete_reference_item.connect("activate", self._delete_reference)
        for item in (
            self.new_reference_item,
            self.edit_reference_item,
            self.duplicate_reference_item,
            self.delete_reference_item,
        ):
            ref_menu.append(item)

        help_item = Gtk.MenuItem(label="Help")
        help_menu = Gtk.Menu()
        help_item.set_submenu(help_menu)
        about = Gtk.MenuItem(label="About")
        about.connect("activate", lambda _item: show_about(self.window))
        help_menu.append(about)

        for item in (file_item, ref_item, help_item):
            menu_bar.append(item)
        return menu_bar

    def _build_search_row(self):
        Gtk = self._Gtk
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box.set_margin_start(8)
        box.set_margin_end(8)
        box.set_margin_top(8)

        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Search references")
        self.search_entry.set_hexpand(True)
        self.search_entry.connect("changed", self._on_search_changed)
        box.pack_start(self.search_entry, True, True, 0)

        self.filter_button = Gtk.MenuButton()
        self.filter_button.set_label("Filters")
        self.filter_popover = Gtk.Popover.new(self.filter_button)
        self.filter_button.set_popover(self.filter_popover)
        filter_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        filter_box.set_border_width(10)
        self.filter_popover.add(filter_box)

        self.filter_combos: dict[str, object] = {}
        specs = (
            ("reference_type", "Type"),
            ("tag", "Tag"),
            ("file", "File"),
            ("integrity", "Integrity"),
            ("sort", "Sort"),
        )
        for name, label_text in specs:
            row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
            label = Gtk.Label(label=label_text, xalign=0)
            label.set_size_request(80, -1)
            combo = Gtk.ComboBoxText()
            combo.set_hexpand(True)
            combo.connect("changed", self._on_filter_changed)
            row.pack_start(label, False, False, 0)
            row.pack_start(combo, True, True, 0)
            filter_box.pack_start(row, False, False, 0)
            self.filter_combos[name] = combo

        self._reset_filter_choices(())
        self.filter_popover.show_all()
        box.pack_start(self.filter_button, False, False, 0)
        return box

    # ---------- public shell boundary ----------
    @property
    def disposed(self) -> bool:
        return self._disposed

    def present(self) -> None:
        self.window.show_all()
        self.window.present()

    def open_library(self, path: str) -> None:
        if not isinstance(path, str) or not path.strip():
            raise ValueError("library path is required")
        if self._search_dispatcher.pending:
            self._search_dispatcher.cancel_pending()
        self.search_entry.set_text("")
        store = MarkdownReferenceStore(path)
        controller = ReferenceController(
            store,
            self.view,
            resolve_conflict=lambda: run_conflict_dialog(self.window),
            on_error=lambda message: show_error(self.window, message),
        )
        self.controller = controller
        self.library_path = store.path
        controller.load()
        self.window.set_title(f"Schedulae — {Path(store.selected_path).name}")
        self._reset_filter_choices(controller.records)
        self._sync_action_state()

    def create_library(self, path: str) -> None:
        created = create_empty_reference_library(path)
        self.open_library(created)

    def action_state(self) -> ShellActionState:
        controller = self.controller
        return compute_action_state(
            library_open=controller is not None,
            read_only=controller.read_only if controller is not None else False,
            selected=bool(controller.selected_key) if controller is not None else False,
        )

    def dispose(self) -> None:
        if self._disposed:
            return
        self._disposed = True
        self._search_dispatcher.dispose()
        self.view.dispose()
        self.controller = None

    # ---------- file workflows ----------
    def _new_library_dialog(self, _item) -> None:
        Gtk = self._Gtk
        dialog = Gtk.FileChooserDialog(
            title="New Reference Library",
            transient_for=self.window,
            action=Gtk.FileChooserAction.SAVE,
        )
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        dialog.add_button("Create", Gtk.ResponseType.OK)
        dialog.set_current_name("references.md")
        dialog.set_do_overwrite_confirmation(False)
        try:
            response = dialog.run()
            filename = dialog.get_filename() if response == Gtk.ResponseType.OK else None
            dialog.hide()
        finally:
            dialog.destroy()
        if not filename:
            return
        try:
            self.create_library(filename)
        except (OSError, TypeError, ValueError) as error:
            show_error(self.window, str(error))

    def _open_library_dialog(self, _item) -> None:
        Gtk = self._Gtk
        dialog = Gtk.FileChooserDialog(
            title="Open Reference Library",
            transient_for=self.window,
            action=Gtk.FileChooserAction.OPEN,
        )
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        dialog.add_button("Open", Gtk.ResponseType.OK)
        filter_md = Gtk.FileFilter()
        filter_md.set_name("Markdown libraries")
        filter_md.add_pattern("*.md")
        dialog.add_filter(filter_md)
        try:
            response = dialog.run()
            filename = dialog.get_filename() if response == Gtk.ResponseType.OK else None
            dialog.hide()
        finally:
            dialog.destroy()
        if filename:
            self.open_library(filename)

    # ---------- reference workflows ----------
    def _new_reference(self, _item=None) -> None:
        controller = self.controller
        if controller is None or controller.read_only:
            return
        record = run_reference_editor(
            self.window,
            initial=ReferenceDraft(),
            existing_identity_keys=controller.identity_keys,
            allow_key_edit=True,
            title="New Reference",
        )
        if record is not None and controller.add(record):
            self._after_mutation()

    def _edit_reference(self, _item=None) -> None:
        controller = self.controller
        if controller is None or controller.read_only:
            return
        original = controller.selected_record()
        if original is None:
            return
        record = run_reference_editor(
            self.window,
            initial=ReferenceDraft.from_record(original),
            existing_identity_keys=tuple(key for key in controller.identity_keys if key not in original.identity_keys),
            allow_key_edit=False,
            title="Edit Reference",
        )
        if record is not None and controller.update(original.key, record):
            self._after_mutation()

    def _duplicate_reference(self, _item=None) -> None:
        controller = self.controller
        if controller is None or controller.read_only:
            return
        original = controller.selected_record()
        if original is None:
            return
        draft_record = duplicate_reference(original, controller.identity_keys)
        record = run_reference_editor(
            self.window,
            initial=ReferenceDraft.from_record(draft_record),
            existing_identity_keys=controller.identity_keys,
            allow_key_edit=True,
            title="Duplicate Reference",
        )
        if record is not None and controller.add(record):
            self._after_mutation()

    def _delete_reference(self, _item=None) -> None:
        controller = self.controller
        if controller is None or controller.read_only:
            return
        record = controller.selected_record()
        if record is None:
            return
        impact = build_delete_impact(controller.records, record.key)
        if not run_delete_confirmation(
            self.window,
            key=record.key,
            impact_lines=impact.summary_lines,
        ):
            return
        if controller.delete(record.key):
            self._after_mutation()

    # ---------- search/filter/selection ----------
    def _on_search_changed(self, entry) -> None:
        if self.controller is not None:
            self._search_dispatcher.submit(entry.get_text())

    def _deliver_query(self, query: str) -> None:
        if self.controller is not None:
            self.controller.set_filters(query=query)
            self._sync_action_state()

    def _on_filter_changed(self, _combo) -> None:
        if self._updating_filters or self.controller is None:
            return
        values = {name: combo.get_active_text() or "all" for name, combo in self.filter_combos.items()}
        self.controller.set_filters(**values)
        self._sync_action_state()

    def _reset_filter_choices(self, records) -> None:
        current = self.controller.filters if self.controller is not None else None
        options = {
            "reference_type": ("all", *available_types(records)),
            "tag": ("all", *available_tags(records)),
            "file": ("all", "present", "missing", "unset"),
            "integrity": ("all", "error", "warning", "clean"),
            "sort": ("author-year-title", "title", "year", "key", "type"),
        }
        desired = {
            "reference_type": current.reference_type if current else "all",
            "tag": current.tag if current else "all",
            "file": current.file if current else "all",
            "integrity": current.integrity if current else "all",
            "sort": current.sort if current else "author-year-title",
        }
        self._updating_filters = True
        try:
            for name, combo in self.filter_combos.items():
                combo.remove_all()
                values = options[name]
                for value in values:
                    combo.append_text(value)
                target = desired[name] if desired[name] in values else values[0]
                combo.set_active(values.index(target))
        finally:
            self._updating_filters = False

    def _on_view_selection_changed(self) -> None:
        if self.controller is not None:
            self.controller.sync_selection_from_view()
            self._sync_action_state()

    def _after_mutation(self) -> None:
        if self.controller is not None:
            self._reset_filter_choices(self.controller.records)
        self._sync_action_state()

    def _sync_action_state(self) -> None:
        state = self.action_state()
        self.new_reference_item.set_sensitive(state.new_reference)
        self.edit_reference_item.set_sensitive(state.edit_reference)
        self.duplicate_reference_item.set_sensitive(state.duplicate_reference)
        self.delete_reference_item.set_sensitive(state.delete_reference)
        self.search_entry.set_sensitive(state.search_filters)
        self.filter_button.set_sensitive(state.search_filters)

    def _on_destroy(self, _window) -> None:
        self.dispose()
