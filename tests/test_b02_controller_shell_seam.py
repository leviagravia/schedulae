# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import unittest

from schedulae.reference_controller import ReferenceController
from schedulae.reference_store import ReferenceLibrarySnapshot, ReferenceSaveResult
from schedulae.research_file import FileToken
from schedulae.references import ReferenceRecord


class Store:
    def __init__(self, snapshot):
        self.snapshot = snapshot
    def load(self):
        return self.snapshot
    def save(self, records, expected_token, *, force=False):
        return ReferenceSaveResult("saved", FileToken(True, 1, 1, "x"))


class View:
    widget = object()
    def __init__(self):
        self.contexts = []
        self.renders = []
        self.detail = []
        self.key = None
    def set_context(self, context):
        self.contexts.append(context)
    def render(self, records, selected_key, status):
        self.renders.append((records, selected_key, status))
        self.key = selected_key
    def selected_key(self):
        return self.key
    def select_key(self, key):
        self.key = key
        return True
    def render_detail(self, record, context):
        self.detail.append((record, context))


class B02ControllerShellSeamTests(unittest.TestCase):
    def test_controller_exposes_read_only_without_leaking_diagnostics_ownership(self):
        snapshot = ReferenceLibrarySnapshot((), FileToken(False), ())
        controller = ReferenceController(Store(snapshot), View(), resolve_conflict=lambda: "cancel", on_error=lambda _m: None)
        controller.load()
        self.assertFalse(controller.read_only)
        self.assertEqual(controller.diagnostics, ())

    def test_controller_pushes_context_before_render(self):
        record = ReferenceRecord("a", "Alpha")
        view = View()
        controller = ReferenceController(
            Store(ReferenceLibrarySnapshot((record,), FileToken(True, 1, 1, "x"), ())),
            view,
            resolve_conflict=lambda: "cancel",
            on_error=lambda _m: None,
        )
        controller.load()
        self.assertTrue(view.contexts)
        self.assertTrue(view.renders)
        self.assertIs(view.contexts[-1], controller.context)

    def test_semantic_selection_owner_remains_controller(self):
        records = (ReferenceRecord("a", "Alpha"), ReferenceRecord("b", "Beta"))
        view = View()
        controller = ReferenceController(
            Store(ReferenceLibrarySnapshot(records, FileToken(True, 1, 1, "x"), ())),
            view,
            resolve_conflict=lambda: "cancel",
            on_error=lambda _m: None,
        )
        controller.load()
        view.key = "b"
        controller.sync_selection_from_view()
        self.assertEqual(controller.selected_key, "b")
        self.assertEqual(controller.selected_record().title, "Beta")


if __name__ == "__main__":
    unittest.main()
