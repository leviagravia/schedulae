# SPDX-License-Identifier: GPL-3.0-or-later
"""Validated draft dialogs for the thin Schedulae GTK3 shell."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from schedulae.references import ReferenceRecord, suggest_reference_key


def _split_semicolon(value: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in value.split(";") if part.strip())


def _split_comma(value: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in value.split(",") if part.strip())


@dataclass(frozen=True)
class ReferenceDraft:
    key: str = ""
    title: str = ""
    type: str = "book"
    authors: str = ""
    year: str = ""
    editors: str = ""
    container_title: str = ""
    publisher: str = ""
    location: str = ""
    volume: str = ""
    issue: str = ""
    pages: str = ""
    doi: str = ""
    isbn: str = ""
    issn: str = ""
    url: str = ""
    language: str = ""
    file_path: str = ""
    tags: str = ""
    annotation: str = ""
    aliases: tuple[str, ...] = ()
    extra_fields: tuple[tuple[str, str], ...] = ()

    @classmethod
    def from_record(cls, record: ReferenceRecord) -> "ReferenceDraft":
        if not isinstance(record, ReferenceRecord):
            raise TypeError("record must be ReferenceRecord")
        return cls(
            key=record.key,
            title=record.title,
            type=record.type,
            authors="; ".join(record.authors),
            year=record.year,
            editors="; ".join(record.editors),
            container_title=record.container_title,
            publisher=record.publisher,
            location=record.location,
            volume=record.volume,
            issue=record.issue,
            pages=record.pages,
            doi=record.doi,
            isbn=record.isbn,
            issn=record.issn,
            url=record.url,
            language=record.language,
            file_path=record.file_path,
            tags=", ".join(record.tags),
            annotation=record.annotation,
            aliases=record.aliases,
            extra_fields=record.extra_fields,
        )

    def to_record(self) -> ReferenceRecord:
        return ReferenceRecord(
            key=self.key,
            title=self.title,
            type=self.type,
            authors=_split_semicolon(self.authors),
            year=self.year,
            editors=_split_semicolon(self.editors),
            container_title=self.container_title,
            publisher=self.publisher,
            location=self.location,
            volume=self.volume,
            issue=self.issue,
            pages=self.pages,
            doi=self.doi,
            isbn=self.isbn,
            issn=self.issn,
            url=self.url,
            language=self.language,
            file_path=self.file_path,
            aliases=self.aliases,
            tags=_split_comma(self.tags),
            annotation=self.annotation,
            extra_fields=self.extra_fields,
        )

    def suggested_key(self, existing_identity_keys: Iterable[str]) -> str:
        return suggest_reference_key(
            _split_semicolon(self.authors),
            self.year,
            self.title,
            existing_identity_keys,
        )


def _gtk():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk
    return Gtk


class ReferenceEditorDialog:
    FIELD_SPECS = (
        ("key", "Citation key"),
        ("type", "Type"),
        ("title", "Title"),
        ("authors", "Authors (; separated)"),
        ("year", "Year / Date"),
        ("editors", "Editors (; separated)"),
        ("container_title", "Container"),
        ("publisher", "Publisher"),
        ("location", "Location"),
        ("volume", "Volume"),
        ("issue", "Issue"),
        ("pages", "Pages"),
        ("doi", "DOI"),
        ("isbn", "ISBN"),
        ("issn", "ISSN"),
        ("url", "URL"),
        ("language", "Language"),
        ("file_path", "Local file"),
        ("tags", "Tags (, separated)"),
    )

    def __init__(
        self,
        parent,
        *,
        initial: ReferenceDraft,
        existing_identity_keys: Iterable[str],
        allow_key_edit: bool,
        title: str,
    ) -> None:
        if not isinstance(initial, ReferenceDraft):
            raise TypeError("initial must be ReferenceDraft")
        Gtk = _gtk()
        self._Gtk = Gtk
        self.initial = initial
        self.existing_identity_keys = tuple(existing_identity_keys)
        self.allow_key_edit = bool(allow_key_edit)

        self.dialog = Gtk.Dialog(
            title=title,
            transient_for=parent,
            modal=True,
            destroy_with_parent=True,
        )
        self.dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.dialog.add_button("Save", Gtk.ResponseType.OK)
        self.dialog.set_default_response(Gtk.ResponseType.OK)
        self.dialog.set_default_size(620, 650)

        content = self.dialog.get_content_area()
        content.set_spacing(8)
        content.set_border_width(10)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        grid = Gtk.Grid(column_spacing=10, row_spacing=6)
        grid.set_hexpand(True)
        scrolled.add(grid)
        content.pack_start(scrolled, True, True, 0)

        self.entries: dict[str, object] = {}
        for row, (name, label_text) in enumerate(self.FIELD_SPECS):
            label = Gtk.Label(label=label_text, xalign=0)
            entry = Gtk.Entry()
            entry.set_text(getattr(initial, name))
            entry.set_hexpand(True)
            if name == "key" and not self.allow_key_edit:
                entry.set_editable(False)
                entry.set_sensitive(False)
            grid.attach(label, 0, row, 1, 1)
            grid.attach(entry, 1, row, 1, 1)
            self.entries[name] = entry

        key_row = next(i for i, spec in enumerate(self.FIELD_SPECS) if spec[0] == "key")
        self.suggest_button = Gtk.Button(label="Suggest")
        self.suggest_button.set_sensitive(self.allow_key_edit)
        self.suggest_button.connect("clicked", self._on_suggest)
        grid.attach(self.suggest_button, 2, key_row, 1, 1)

        ann_row = len(self.FIELD_SPECS)
        grid.attach(Gtk.Label(label="Annotation", xalign=0), 0, ann_row, 1, 1)
        self.annotation = Gtk.TextView()
        self.annotation.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        self.annotation.get_buffer().set_text(initial.annotation)
        ann_scroll = Gtk.ScrolledWindow()
        ann_scroll.set_min_content_height(120)
        ann_scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        ann_scroll.add(self.annotation)
        grid.attach(ann_scroll, 1, ann_row, 2, 1)

        self.error_label = Gtk.Label(xalign=0)
        self.error_label.set_line_wrap(True)
        content.pack_start(self.error_label, False, False, 0)

        self.dialog.show_all()

    def _current_draft(self) -> ReferenceDraft:
        values = {name: entry.get_text() for name, entry in self.entries.items()}
        buffer = self.annotation.get_buffer()
        annotation = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        return ReferenceDraft(
            **values,
            annotation=annotation,
            aliases=self.initial.aliases,
            extra_fields=self.initial.extra_fields,
        )

    def _on_suggest(self, _button) -> None:
        draft = self._current_draft()
        self.entries["key"].set_text(draft.suggested_key(self.existing_identity_keys))

    def build_result(self) -> ReferenceRecord | None:
        try:
            record = self._current_draft().to_record()
        except (TypeError, ValueError) as error:
            self.error_label.set_text(str(error))
            return None
        if self.allow_key_edit:
            other = set(self.existing_identity_keys)
            for identity in record.identity_keys:
                if identity in other:
                    self.error_label.set_text(f"Reference identity already exists: {identity}")
                    return None
        self.error_label.set_text("")
        return record


def run_reference_editor(
    parent,
    *,
    initial: ReferenceDraft,
    existing_identity_keys: Iterable[str],
    allow_key_edit: bool,
    title: str,
) -> ReferenceRecord | None:
    Gtk = _gtk()
    editor = ReferenceEditorDialog(
        parent,
        initial=initial,
        existing_identity_keys=existing_identity_keys,
        allow_key_edit=allow_key_edit,
        title=title,
    )
    result: ReferenceRecord | None = None
    try:
        while True:
            response = editor.dialog.run()
            if response != Gtk.ResponseType.OK:
                break
            candidate = editor.build_result()
            if candidate is not None:
                result = candidate
                break
        editor.dialog.hide()
        return result
    finally:
        editor.dialog.destroy()


def build_delete_dialog(parent, *, key: str, impact_lines: Iterable[str]):
    Gtk = _gtk()
    detail = "\n".join(line for line in impact_lines if line)
    secondary = f"Delete reference {key}?"
    if detail:
        secondary += "\n\n" + detail + "\n\nRelated entries are not changed automatically."
    dialog = Gtk.MessageDialog(
        transient_for=parent,
        modal=True,
        destroy_with_parent=True,
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.NONE,
        text="Delete Reference",
    )
    dialog.format_secondary_text(secondary)
    dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
    dialog.add_button("Delete", Gtk.ResponseType.OK)
    return dialog


def run_delete_confirmation(parent, *, key: str, impact_lines: Iterable[str]) -> bool:
    Gtk = _gtk()
    dialog = build_delete_dialog(parent, key=key, impact_lines=impact_lines)
    try:
        response = dialog.run()
        dialog.hide()
        return response == Gtk.ResponseType.OK
    finally:
        dialog.destroy()


def conflict_choice_from_response(response: int) -> str:
    Gtk = _gtk()
    if response == Gtk.ResponseType.YES:
        return "reload"
    if response == Gtk.ResponseType.APPLY:
        return "overwrite"
    return "cancel"


def build_conflict_dialog(parent):
    Gtk = _gtk()
    dialog = Gtk.MessageDialog(
        transient_for=parent,
        modal=True,
        destroy_with_parent=True,
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.NONE,
        text="Reference Library Changed",
    )
    dialog.format_secondary_text(
        "The library changed outside Schedulae. Reload the external version, overwrite it explicitly, or cancel."
    )
    dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
    dialog.add_button("Reload", Gtk.ResponseType.YES)
    dialog.add_button("Overwrite", Gtk.ResponseType.APPLY)
    return dialog


def run_conflict_dialog(parent) -> str:
    dialog = build_conflict_dialog(parent)
    try:
        response = dialog.run()
        dialog.hide()
        return conflict_choice_from_response(response)
    finally:
        dialog.destroy()


def show_error(parent, message: str) -> None:
    Gtk = _gtk()
    dialog = Gtk.MessageDialog(
        transient_for=parent,
        modal=True,
        destroy_with_parent=True,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.CLOSE,
        text="Schedulae",
    )
    dialog.format_secondary_text(message if isinstance(message, str) else str(message))
    try:
        dialog.run()
        dialog.hide()
    finally:
        dialog.destroy()


def show_about(parent) -> None:
    Gtk = _gtk()
    dialog = Gtk.AboutDialog(transient_for=parent, modal=True, destroy_with_parent=True)
    dialog.set_program_name("Schedulae")
    dialog.set_comments(
        "A lightweight, local-first desktop bibliography and citation manager for scholarly references, metadata, notes, and BibTeX/BibLaTeX workflows."
    )
    dialog.set_license_type(Gtk.License.GPL_3_0)
    dialog.set_website("https://github.com/leviagravia/schedulae")
    try:
        dialog.run()
        dialog.hide()
    finally:
        dialog.destroy()
