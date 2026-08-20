# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import os
from pathlib import Path
import stat
import tempfile
import unittest

from schedulae.reference_store import MarkdownReferenceStore, create_empty_reference_library


class B02EmptyLibraryTests(unittest.TestCase):
    def test_create_empty_library_is_immediately_valid(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "library.md"
            created = create_empty_reference_library(str(path))
            self.assertEqual(created, str(path.resolve()))
            self.assertEqual(path.read_text(encoding="utf-8"), "# Calamus References v1\n")
            snapshot = MarkdownReferenceStore(str(path)).load()
            self.assertEqual(snapshot.records, ())
            self.assertEqual(snapshot.diagnostics, ())
            self.assertTrue(snapshot.token.exists)

    def test_create_empty_library_refuses_existing_regular_file(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "library.md"
            path.write_text("KEEP", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                create_empty_reference_library(str(path))
            self.assertEqual(path.read_text(encoding="utf-8"), "KEEP")

    def test_create_empty_library_refuses_existing_symlink(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            victim = root / "victim.md"
            victim.write_text("KEEP", encoding="utf-8")
            link = root / "library.md"
            link.symlink_to(victim)
            with self.assertRaises(FileExistsError):
                create_empty_reference_library(str(link))
            self.assertTrue(link.is_symlink())
            self.assertEqual(victim.read_text(encoding="utf-8"), "KEEP")

    def test_create_empty_library_refuses_broken_symlink(self):
        with tempfile.TemporaryDirectory() as td:
            link = Path(td) / "library.md"
            link.symlink_to(Path(td) / "missing.md")
            with self.assertRaises(FileExistsError):
                create_empty_reference_library(str(link))
            self.assertTrue(link.is_symlink())

    def test_create_empty_library_is_private(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "library.md"
            create_empty_reference_library(str(path))
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)

    def test_create_empty_library_validates_path(self):
        with self.assertRaises(TypeError):
            create_empty_reference_library(None)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            create_empty_reference_library("   ")


if __name__ == "__main__":
    unittest.main()
