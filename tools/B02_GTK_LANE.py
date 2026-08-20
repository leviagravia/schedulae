#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""One fresh-process real-GTK validation lane for Schedulae B02."""
from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gio, GLib, Gtk

from schedulae.bibliography import build_delete_impact
from schedulae.gtk_app import SchedulaeApplication
from schedulae.gtk_dialogs import (
    ReferenceDraft,
    ReferenceEditorDialog,
    build_conflict_dialog,
    build_delete_dialog,
    conflict_choice_from_response,
)
from schedulae.gtk_reference_view import GtkReferenceView
from schedulae.gtk_window import SchedulaeWindow
from schedulae.reference_store import serialize_references_markdown
from schedulae.references import ReferenceRecord


def fail(message: str) -> int:
    print("GTK_LANE=FAIL")
    print(f"ERR={message}")
    return 1


def run_main_window(check, *, timeout_ms: int = 1500) -> int:
    window = Gtk.Window()
    state = {"done": False, "rc": 1, "err": "timeout"}

    def validate():
        if state["done"]:
            return False
        try:
            check(window)
            state.update(done=True, rc=0, err="NONE")
        except BaseException as error:
            state.update(done=True, rc=1, err=f"{type(error).__name__}:{error}")
        window.destroy()
        Gtk.main_quit()
        return False

    def timeout():
        if not state["done"]:
            state.update(done=True, rc=1, err="timeout")
            window.destroy()
            Gtk.main_quit()
        return False

    window.show_all()
    GLib.timeout_add(40, validate)
    GLib.timeout_add(timeout_ms, timeout)
    Gtk.main()
    if state["rc"]:
        return fail(state["err"])
    return 0


def app_for_shell():
    app = Gtk.Application(application_id=None, flags=Gio.ApplicationFlags.NON_UNIQUE)
    if not app.register(None):
        raise RuntimeError("Gtk.Application registration failed")
    return app


def lane_view_selection() -> int:
    def check(window):
        view = GtkReferenceView()
        window.add(view.widget)
        records = (
            ReferenceRecord("alpha", "Alpha", authors=("Doe, Jane",), year="2026"),
            ReferenceRecord("beta", "Beta", authors=("Roe, John",), year="2025"),
        )
        callbacks = []
        view.set_selection_changed(lambda: callbacks.append(view.selected_key()))
        view.render(records, "beta", "2 reference(s).")
        view.render_detail(records[1], __import__("schedulae.bibliography", fromlist=["BibliographyContext"]).BibliographyContext())
        window.show_all()
        if view.model.iter_n_children(None) != 2:
            raise AssertionError("row count")
        if view.selected_key() != "beta":
            raise AssertionError("selection restore")
        if callbacks:
            raise AssertionError("render emitted semantic selection callback")
        view.select_key("alpha")
        if view.selected_key() != "alpha":
            raise AssertionError("select_key")
        view.dispose()
    return run_main_window(check)


def lane_window_shell() -> int:
    app = app_for_shell()
    shell = SchedulaeWindow(app)
    state = {"rc": 1, "err": "timeout"}

    def check():
        try:
            if shell.action_state().search_filters:
                raise AssertionError("search enabled without library")
            if shell.window.get_application() is not app:
                raise AssertionError("application ownership")
            state.update(rc=0, err="NONE")
        except BaseException as error:
            state.update(rc=1, err=f"{type(error).__name__}:{error}")
        shell.window.destroy()
        Gtk.main_quit()
        return False

    shell.window.show_all()
    GLib.timeout_add(50, check)
    GLib.timeout_add(1500, lambda: (shell.window.destroy(), Gtk.main_quit(), False)[-1])
    Gtk.main()
    return 0 if state["rc"] == 0 else fail(state["err"])


def make_library(path: Path) -> None:
    records = (
        ReferenceRecord("alpha", "Alpha Study", type="article", authors=("Doe, Jane",), year="2026", tags=("A",)),
        ReferenceRecord("beta", "Beta Book", type="book", authors=("Roe, John",), year="2025", tags=("B",)),
        ReferenceRecord("gamma", "Gamma Notes", type="article", authors=("Doe, Jane",), year="2024", tags=("A",)),
    )
    path.write_text(serialize_references_markdown(records), encoding="utf-8")


def lane_library_open() -> int:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "refs.md"
        make_library(path)
        app = app_for_shell()
        shell = SchedulaeWindow(app)
        shell.open_library(str(path))
        state = {"rc": 1, "err": "timeout"}

        def check():
            try:
                if shell.controller is None or not shell.controller.loaded:
                    raise AssertionError("controller not loaded")
                if shell.view.model.iter_n_children(None) != 3:
                    raise AssertionError("list projection")
                if not shell.controller.selected_key:
                    raise AssertionError("semantic selection")
                if not shell.action_state().edit_reference:
                    raise AssertionError("action sensitivity")
                state.update(rc=0, err="NONE")
            except BaseException as error:
                state.update(rc=1, err=f"{type(error).__name__}:{error}")
            shell.window.destroy(); Gtk.main_quit(); return False

        shell.window.show_all()
        GLib.timeout_add(50, check)
        Gtk.main()
        return 0 if state["rc"] == 0 else fail(state["err"])


def lane_search_filter() -> int:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "refs.md"
        make_library(path)
        app = app_for_shell()
        shell = SchedulaeWindow(app)
        shell.open_library(str(path))
        shell.window.show_all()
        state = {"rc": 1, "err": "timeout", "done": False}
        deadline = time.monotonic() + 1.5

        # Two immediate text mutations exercise latest-generation ownership.
        # Gtk.SearchEntry.changed is immediate; the only debounce owner is the
        # explicit 150 ms CoalescedQueryDispatcher.
        shell.search_entry.set_text("beta")
        shell.search_entry.set_text("alpha")

        def finish(rc: int, err: str):
            if state["done"]:
                return False
            state.update(done=True, rc=rc, err=err)
            shell.window.destroy()
            Gtk.main_quit()
            return False

        def poll_semantic_completion():
            try:
                deliveries = shell._search_dispatcher.delivery_count
                if deliveries > 1:
                    return finish(1, f"delivery_count={deliveries}")

                search_complete = (
                    deliveries == 1
                    and not shell._search_dispatcher.pending
                    and shell._search_dispatcher.last_delivered_query == "alpha"
                    and shell.controller.filters.query == "alpha"
                    and shell.view.model.iter_n_children(None) == 1
                )
                if search_complete:
                    type_combo = shell.filter_combos["reference_type"]
                    model = type_combo.get_model()
                    values = []
                    tree_iter = model.get_iter_first()
                    while tree_iter is not None:
                        values.append(model.get_value(tree_iter, 0))
                        tree_iter = model.iter_next(tree_iter)
                    type_combo.set_active(values.index("article"))
                    if shell.controller.filters.reference_type != "article":
                        return finish(1, "type filter")
                    return finish(0, "NONE")

                if time.monotonic() >= deadline:
                    return finish(
                        1,
                        "bounded_timeout:"
                        f"delivery_count={deliveries}:"
                        f"query={shell.controller.filters.query!r}:"
                        f"rows={shell.view.model.iter_n_children(None)}",
                    )
                return True
            except BaseException as error:
                return finish(1, f"{type(error).__name__}:{error}")

        GLib.timeout_add(10, poll_semantic_completion)
        Gtk.main()
        return 0 if state["rc"] == 0 else fail(state["err"])


def lane_new_dialog() -> int:
    def check(window):
        editor = ReferenceEditorDialog(
            window,
            initial=ReferenceDraft(),
            existing_identity_keys=("taken",),
            allow_key_edit=True,
            title="New Reference",
        )
        editor.entries["key"].set_text("new-key")
        editor.entries["title"].set_text("New Title")
        editor.entries["authors"].set_text("Doe, Jane")
        record = editor.build_result()
        if record is None or record.key != "new-key" or record.title != "New Title":
            raise AssertionError("new draft")
        if not editor.entries["key"].get_editable():
            raise AssertionError("new key not editable")
        editor.dialog.hide(); editor.dialog.destroy()
    return run_main_window(check)


def lane_edit_duplicate_dialog() -> int:
    def check(window):
        original = ReferenceRecord("alpha", "Alpha", aliases=("old",), extra_fields=(("Custom", "X"),))
        editor = ReferenceEditorDialog(
            window,
            initial=ReferenceDraft.from_record(original),
            existing_identity_keys=(),
            allow_key_edit=False,
            title="Edit Reference",
        )
        if editor.entries["key"].get_editable() or editor.entries["key"].get_sensitive():
            raise AssertionError("edit key mutable")
        editor.entries["title"].set_text("Changed")
        record = editor.build_result()
        if record is None or record.aliases != original.aliases or record.extra_fields != original.extra_fields:
            raise AssertionError("edit preservation")
        editor.dialog.hide(); editor.dialog.destroy()
    return run_main_window(check)


def lane_delete_dialog() -> int:
    def check(window):
        records = (ReferenceRecord("a", "A"), ReferenceRecord("b", "B", extra_fields=(("Related Keys", "a"),)))
        impact = build_delete_impact(records, "a")
        dialog = build_delete_dialog(window, key="a", impact_lines=impact.summary_lines)
        if not dialog.get_modal() or dialog.get_transient_for() is not window:
            raise AssertionError("delete modal ownership")
        GLib.idle_add(lambda: (dialog.response(Gtk.ResponseType.CANCEL), False)[1])
        response = dialog.run()
        dialog.hide(); dialog.destroy()
        if response != Gtk.ResponseType.CANCEL:
            raise AssertionError("delete response")
    return run_main_window(check)


def lane_conflict_dialog() -> int:
    def check(window):
        dialog = build_conflict_dialog(window)
        if not dialog.get_modal() or dialog.get_transient_for() is not window:
            raise AssertionError("conflict modal ownership")
        GLib.idle_add(lambda: (dialog.response(Gtk.ResponseType.YES), False)[1])
        response = dialog.run()
        dialog.hide(); dialog.destroy()
        if conflict_choice_from_response(response) != "reload":
            raise AssertionError("conflict semantic result")
    return run_main_window(check)


def lane_malformed_read_only() -> int:
    import schedulae.gtk_window as window_module
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.md"
        path.write_text("# Wrong\n", encoding="utf-8")
        messages = []
        old = window_module.show_error
        window_module.show_error = lambda _parent, message: messages.append(message)
        try:
            app = app_for_shell(); shell = SchedulaeWindow(app); shell.open_library(str(path))
            if shell.controller is None or not shell.controller.read_only:
                return fail("malformed library not read-only")
            state = shell.action_state()
            if state.new_reference or state.delete_reference or not state.search_filters:
                return fail("read-only sensitivity")
            if not messages:
                return fail("diagnostic not surfaced")
            shell.window.destroy(); shell.dispose()
            return 0
        finally:
            window_module.show_error = old


def lane_true_application() -> int:
    wrapper = SchedulaeApplication()
    started = time.monotonic()
    state = {"rc": 1, "err": "timeout"}

    def poll():
        if wrapper.window is not None and wrapper.window.window.get_mapped():
            state.update(rc=0, err="NONE")
            wrapper.window.window.close()
            wrapper.application.quit()
            return False
        if time.monotonic() - started > 2.5:
            state.update(rc=1, err="window_not_mapped")
            wrapper.application.quit()
            return False
        return True

    GLib.timeout_add(20, poll)
    wrapper.run([sys.argv[0]])
    return 0 if state["rc"] == 0 else fail(state["err"])


LANES = {
    "view-selection": lane_view_selection,
    "window-shell": lane_window_shell,
    "library-open": lane_library_open,
    "search-filter": lane_search_filter,
    "new-dialog": lane_new_dialog,
    "edit-duplicate-dialog": lane_edit_duplicate_dialog,
    "delete-dialog": lane_delete_dialog,
    "conflict-dialog": lane_conflict_dialog,
    "malformed-read-only": lane_malformed_read_only,
    "true-application": lane_true_application,
}


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in LANES:
        print("ERR=unknown_lane")
        return 2
    name = sys.argv[1]
    print(f"GTK_LANE={name}")
    rc = LANES[name]()
    if rc == 0:
        print("GTK_LANE_RESULT=PASS")
        print("EXIT=0")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
