# SPDX-License-Identifier: GPL-3.0-or-later
"""Thin GTK3 list/detail adapter for the Schedulae reference controller."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from schedulae.bibliography import BibliographyContext, format_reference_detail
from schedulae.references import ReferenceRecord


@dataclass(frozen=True)
class ProjectionRow:
    key: str
    author: str
    year: str
    title: str
    reference_type: str
    integrity: str


def projection_rows(
    records: Iterable[ReferenceRecord],
    context: BibliographyContext = BibliographyContext(),
) -> tuple[ProjectionRow, ...]:
    rows: list[ProjectionRow] = []
    for record in records:
        if not isinstance(record, ReferenceRecord):
            raise TypeError("records must contain ReferenceRecord values")
        rows.append(ProjectionRow(
            key=record.key,
            author=record.primary_author or "Unknown author",
            year=record.year,
            title=record.title,
            reference_type=record.type,
            integrity=", ".join(context.severities(record.key)) or "clean",
        ))
    return tuple(rows)


def restored_selection_key(rows: Iterable[ProjectionRow], selected_key: str | None) -> str | None:
    keys = tuple(row.key for row in rows)
    return selected_key if selected_key in keys else None


def _gtk():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk
    return Gtk


class GtkReferenceView:
    """Persistent ListStore/TreeSelection projection; never owns semantic selection."""

    COL_KEY = 0
    COL_AUTHOR = 1
    COL_YEAR = 2
    COL_TITLE = 3
    COL_TYPE = 4
    COL_INTEGRITY = 5

    def __init__(self) -> None:
        Gtk = _gtk()
        self._Gtk = Gtk
        self._selection_changed: Callable[[], None] = lambda: None
        self._rendering = False
        self._context = BibliographyContext()

        self.model = Gtk.ListStore(str, str, str, str, str, str)
        self.tree = Gtk.TreeView(model=self.model)
        self.tree.set_headers_visible(True)
        self.tree.set_enable_search(False)

        specs = (
            ("Author", self.COL_AUTHOR, False),
            ("Year", self.COL_YEAR, False),
            ("Title", self.COL_TITLE, True),
            ("Type", self.COL_TYPE, False),
        )
        for title, index, expand in specs:
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=index)
            column.set_resizable(True)
            column.set_expand(expand)
            self.tree.append_column(column)

        self.selection = self.tree.get_selection()
        self.selection.set_mode(Gtk.SelectionMode.SINGLE)
        self._selection_handler_id = self.selection.connect("changed", self._on_selection_changed)

        left_scroll = Gtk.ScrolledWindow()
        left_scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        left_scroll.add(self.tree)

        self.detail = Gtk.TextView()
        self.detail.set_editable(False)
        self.detail.set_cursor_visible(True)
        self.detail.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        self.detail.set_left_margin(10)
        self.detail.set_right_margin(10)
        self.detail.set_top_margin(8)
        self.detail.set_bottom_margin(8)
        right_scroll = Gtk.ScrolledWindow()
        right_scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        right_scroll.add(self.detail)

        paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        paned.pack1(left_scroll, resize=True, shrink=False)
        paned.pack2(right_scroll, resize=True, shrink=False)
        paned.set_position(420)

        self.status_label = Gtk.Label(xalign=0)
        self.status_label.set_margin_start(8)
        self.status_label.set_margin_end(8)
        self.status_label.set_margin_top(4)
        self.status_label.set_margin_bottom(4)

        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        root.pack_start(paned, True, True, 0)
        root.pack_start(self.status_label, False, False, 0)
        self._widget = root

    @property
    def widget(self):
        return self._widget

    def set_context(self, context: BibliographyContext) -> None:
        if not isinstance(context, BibliographyContext):
            raise TypeError("context must be BibliographyContext")
        self._context = context

    def set_selection_changed(self, callback: Callable[[], None]) -> None:
        if not callable(callback):
            raise TypeError("callback must be callable")
        self._selection_changed = callback

    def _on_selection_changed(self, _selection) -> None:
        if not self._rendering:
            self._selection_changed()

    def render(
        self,
        records: tuple[ReferenceRecord, ...],
        selected_key: str | None,
        status: str,
    ) -> None:
        rows = projection_rows(records, self._context)
        self._rendering = True
        self.selection.handler_block(self._selection_handler_id)
        try:
            self.model.clear()
            selected_iter = None
            for row in rows:
                tree_iter = self.model.append((
                    row.key,
                    row.author,
                    row.year,
                    row.title,
                    row.reference_type,
                    row.integrity,
                ))
                if row.key == selected_key:
                    selected_iter = tree_iter
            self.selection.unselect_all()
            if selected_iter is not None:
                self.selection.select_iter(selected_iter)
        finally:
            self.selection.handler_unblock(self._selection_handler_id)
            self._rendering = False
        self.status_label.set_text(status if isinstance(status, str) else "")

    def selected_key(self) -> str | None:
        model, tree_iter = self.selection.get_selected()
        if tree_iter is None:
            return None
        return model.get_value(tree_iter, self.COL_KEY)

    def select_key(self, key: str | None) -> bool:
        if key is None:
            self.selection.unselect_all()
            return True
        tree_iter = self.model.get_iter_first()
        while tree_iter is not None:
            if self.model.get_value(tree_iter, self.COL_KEY) == key:
                self.selection.select_iter(tree_iter)
                return True
            tree_iter = self.model.iter_next(tree_iter)
        return False

    def render_detail(
        self,
        record: ReferenceRecord | None,
        context: BibliographyContext,
    ) -> None:
        self._context = context
        text = "No reference selected." if record is None else format_reference_detail(record, context)
        self.detail.get_buffer().set_text(text)

    def dispose(self) -> None:
        if self._selection_handler_id:
            try:
                self.selection.disconnect(self._selection_handler_id)
            except (TypeError, RuntimeError):
                pass
            self._selection_handler_id = 0
        self._selection_changed = lambda: None
