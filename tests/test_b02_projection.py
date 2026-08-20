# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import unittest

from schedulae.bibliography import BibliographyContext
from schedulae.gtk_reference_view import projection_rows, restored_selection_key
from schedulae.references import ReferenceRecord


class B02ProjectionTests(unittest.TestCase):
    def test_projection_uses_canonical_key_as_identity(self):
        records = (ReferenceRecord("a", "Alpha", authors=("Doe, Jane",), year="2026"),)
        rows = projection_rows(records)
        self.assertEqual(rows[0].key, "a")
        self.assertEqual(rows[0].author, "Doe, Jane")
        self.assertEqual(rows[0].year, "2026")
        self.assertEqual(rows[0].title, "Alpha")

    def test_projection_marks_unknown_author_without_mutating_record(self):
        record = ReferenceRecord("a", "Alpha")
        row = projection_rows((record,))[0]
        self.assertEqual(row.author, "Unknown author")
        self.assertEqual(record.authors, ())

    def test_projection_carries_objective_integrity(self):
        record = ReferenceRecord("a", "Alpha")
        context = BibliographyContext((("a", ("error", "warning")),))
        self.assertEqual(projection_rows((record,), context)[0].integrity, "error, warning")

    def test_restore_selection_keeps_visible_key_only(self):
        rows = projection_rows((ReferenceRecord("a", "A"), ReferenceRecord("b", "B")))
        self.assertEqual(restored_selection_key(rows, "b"), "b")
        self.assertIsNone(restored_selection_key(rows, "missing"))

    def test_projection_rejects_non_records(self):
        with self.assertRaises(TypeError):
            projection_rows(("bad",))  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
