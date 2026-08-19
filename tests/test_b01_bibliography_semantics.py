# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from schedulae.bibliography import (
    BibliographyFilters,
    build_bibliography_context,
    build_delete_impact,
    format_reference_detail,
    project_references,
)
from schedulae.references import ReferenceRecord


class B01BibliographySemanticsTests(unittest.TestCase):
    def record(self, key, title, **changes):
        values = dict(key=key, title=title)
        values.update(changes)
        return ReferenceRecord(**values)

    def test_use_filter_is_removed(self):
        self.assertFalse(hasattr(BibliographyFilters(), "use"))
        with self.assertRaises(TypeError):
            BibliographyFilters(use="unused")
        with self.assertRaises(ValueError):
            BibliographyFilters(integrity="advisory")

    def test_detail_has_no_calamus_only_context_labels(self):
        record = self.record("a", "A")
        detail = format_reference_detail(record, build_bibliography_context((record,)))
        self.assertNotIn("Current Document", detail)
        self.assertNotIn("Source Notes", detail)
        self.assertNotIn("Reference Sets", detail)
        self.assertIn("Integrity: clean", detail)

    def test_absent_author_year_tags_and_identifiers_are_not_integrity_issues(self):
        record = self.record("a", "A")
        context = build_bibliography_context((record,))
        self.assertEqual(context.severities("a"), ())

    def test_duplicate_identifier_is_objective_error(self):
        records = (
            self.record("a", "A", doi="10.1000/ABC"),
            self.record("b", "B", doi="10.1000/abc"),
        )
        context = build_bibliography_context(records)
        self.assertEqual(context.severities("a"), ("error",))
        self.assertEqual(context.severities("b"), ("error",))
        visible = project_references(records, BibliographyFilters(integrity="error"), context)
        self.assertEqual(tuple(r.key for r in visible), ("a", "b"))

    def test_missing_local_file_is_warning_but_unset_file_is_clean(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = str(Path(tmp) / "missing.pdf")
            records = (self.record("a", "A", file_path=missing), self.record("b", "B"))
            context = build_bibliography_context(records)
            self.assertEqual(context.severities("a"), ("warning",))
            self.assertEqual(context.severities("b"), ())

    def test_related_reference_integrity_is_included(self):
        records = (
            self.record("a", "A", extra_fields=(("Related Keys", "missing"),)),
            self.record("b", "B"),
        )
        context = build_bibliography_context(records)
        self.assertIn("error", context.severities("a"))

    def test_delete_impact_only_reports_real_related_references(self):
        records = (
            self.record("a", "A"),
            self.record("b", "B", extra_fields=(("Related Keys", "a"),)),
        )
        impact = build_delete_impact(records, "a")
        self.assertEqual(impact.related_reference_owners, ("b",))
        self.assertEqual(impact.summary_lines, ("Related from: b",))
        with self.assertRaises(TypeError):
            build_delete_impact(records, "a", document_text="[@a]")

    def test_search_type_tag_file_integrity_sort_projection_remains_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            present = Path(tmp) / "present.pdf"
            present.write_text("x", encoding="utf-8")
            records = (
                self.record("b", "Beta", type="article", tags=("Faith",), file_path=str(present), authors=("Zulu",)),
                self.record("a", "Alpha", type="book", tags=("Study",), authors=("Alpha",)),
            )
            context = build_bibliography_context(records)
            self.assertEqual(tuple(r.key for r in project_references(records, BibliographyFilters(query="alpha"), context)), ("a",))
            self.assertEqual(tuple(r.key for r in project_references(records, BibliographyFilters(reference_type="article"), context)), ("b",))
            self.assertEqual(tuple(r.key for r in project_references(records, BibliographyFilters(tag="faith"), context)), ("b",))
            self.assertEqual(tuple(r.key for r in project_references(records, BibliographyFilters(file="present"), context)), ("b",))
            self.assertEqual(tuple(r.key for r in project_references(records, BibliographyFilters(sort="key"), context)), ("a", "b"))


if __name__ == "__main__":
    unittest.main()
