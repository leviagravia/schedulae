# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from dataclasses import replace
import unittest

from schedulae.bibliography import duplicate_reference
from schedulae.gtk_dialogs import ReferenceDraft
from schedulae.references import ReferenceRecord


class B02DraftTests(unittest.TestCase):
    def _record(self):
        return ReferenceRecord(
            key="doe2026alpha",
            title="Alpha",
            type="article",
            authors=("Doe, Jane", "Roe, John"),
            year="2026",
            editors=("Editor, Eve",),
            container_title="Journal",
            publisher="Publisher",
            location="Rome",
            volume="2",
            issue="3",
            pages="10-20",
            doi="10.1/example",
            isbn="9780000000000",
            issn="1234-5678",
            url="https://example.invalid",
            language="en",
            file_path="/tmp/paper.pdf",
            aliases=("old-key",),
            tags=("One", "Two"),
            annotation="Line one\nLine two",
            extra_fields=(("Custom", "Value"), ("Related Keys", "other")),
        )

    def test_record_to_draft_to_record_preserves_semantics(self):
        record = self._record()
        self.assertEqual(ReferenceDraft.from_record(record).to_record(), record)

    def test_draft_parses_authors_editors_and_tags(self):
        draft = ReferenceDraft(
            key="a2026work", title="Work", authors="Doe, Jane; Roe, John",
            editors="Editor, Eve", tags="Alpha, Beta",
        )
        record = draft.to_record()
        self.assertEqual(record.authors, ("Doe, Jane", "Roe, John"))
        self.assertEqual(record.editors, ("Editor, Eve",))
        self.assertEqual(record.tags, ("Alpha", "Beta"))

    def test_invalid_complete_draft_fails_before_commit(self):
        with self.assertRaises(ValueError):
            ReferenceDraft(key="valid", title="").to_record()

    def test_suggested_key_is_library_aware(self):
        draft = ReferenceDraft(title="Alpha Study", authors="Jane Doe", year="2026")
        first = draft.suggested_key(())
        second = draft.suggested_key((first,))
        self.assertNotEqual(first, second)
        self.assertTrue(second.startswith(first))

    def test_duplicate_draft_has_new_key_and_no_aliases(self):
        record = self._record()
        duplicate = duplicate_reference(record, record.identity_keys)
        self.assertNotEqual(duplicate.key, record.key)
        self.assertEqual(duplicate.aliases, ())
        self.assertEqual(duplicate.title, record.title)

    def test_edit_draft_preserves_unknown_fields_and_aliases(self):
        original = self._record()
        draft = replace(ReferenceDraft.from_record(original), title="Changed")
        edited = draft.to_record()
        self.assertEqual(edited.key, original.key)
        self.assertEqual(edited.aliases, original.aliases)
        self.assertEqual(edited.extra_fields, original.extra_fields)
        self.assertEqual(edited.title, "Changed")

    def test_cancel_model_is_zero_mutation_by_construction(self):
        original = self._record()
        draft = replace(ReferenceDraft.from_record(original), title="Not committed")
        self.assertEqual(original.title, "Alpha")
        self.assertEqual(draft.title, "Not committed")


if __name__ == "__main__":
    unittest.main()
