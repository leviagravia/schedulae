# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import importlib
from pathlib import Path
import unittest

import schedulae
from schedulae.gtk_app import APPLICATION_ID
from schedulae.gtk_window import compute_action_state


class B02ShellContractTests(unittest.TestCase):
    def test_shell_modules_import_without_loading_gi(self):
        for name in ("gtk_app", "gtk_window", "gtk_reference_view", "gtk_dialogs"):
            importlib.import_module(f"schedulae.{name}")

    def test_application_id_is_frozen(self):
        self.assertEqual(APPLICATION_ID, "io.github.leviagravia.Schedulae")

    def test_no_library_disables_reference_actions_and_search(self):
        state = compute_action_state(library_open=False, read_only=False, selected=False)
        self.assertFalse(state.new_reference)
        self.assertFalse(state.edit_reference)
        self.assertFalse(state.search_filters)

    def test_valid_empty_library_enables_new_and_search_only(self):
        state = compute_action_state(library_open=True, read_only=False, selected=False)
        self.assertTrue(state.new_reference)
        self.assertTrue(state.search_filters)
        self.assertFalse(state.edit_reference)
        self.assertFalse(state.delete_reference)

    def test_valid_selection_enables_all_reference_actions(self):
        state = compute_action_state(library_open=True, read_only=False, selected=True)
        self.assertTrue(state.new_reference)
        self.assertTrue(state.edit_reference)
        self.assertTrue(state.duplicate_reference)
        self.assertTrue(state.delete_reference)

    def test_read_only_library_disables_mutation_but_keeps_search(self):
        state = compute_action_state(library_open=True, read_only=True, selected=True)
        self.assertFalse(state.new_reference)
        self.assertFalse(state.edit_reference)
        self.assertFalse(state.duplicate_reference)
        self.assertFalse(state.delete_reference)
        self.assertTrue(state.search_filters)

    def test_shell_source_has_no_manual_event_pumping_or_focus_scroll_correctness(self):
        root = Path(schedulae.__file__).parent
        text = "\n".join((root / name).read_text(encoding="utf-8") for name in (
            "gtk_app.py", "gtk_window.py", "gtk_reference_view.py", "gtk_dialogs.py",
        ))
        for forbidden in ("Gtk.events_pending", "main_iteration", "scroll_to_cell", "grab_focus"):
            self.assertNotIn(forbidden, text)

    def test_search_entry_uses_changed_with_explicit_coalescer(self):
        root = Path(schedulae.__file__).parent
        text = (root / "gtk_window.py").read_text(encoding="utf-8")
        self.assertIn('self.search_entry.connect("changed", self._on_search_changed)', text)
        self.assertNotIn('self.search_entry.connect("search-changed", self._on_search_changed)', text)

    def test_domain_modules_remain_free_of_gi_imports(self):
        root = Path(schedulae.__file__).parent
        domain = (
            "bibliography.py", "bibliography_search.py", "bibtex.py", "bibtex_controller.py",
            "bibtex_import_session.py", "citations.py", "reference_controller.py",
            "reference_store.py", "references.py", "related_references.py", "research_file.py",
        )
        for name in domain:
            text = (root / name).read_text(encoding="utf-8")
            self.assertNotIn("import gi", text, name)
            self.assertNotIn("from gi", text, name)


if __name__ == "__main__":
    unittest.main()
