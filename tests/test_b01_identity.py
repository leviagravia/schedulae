# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import inspect
from pathlib import Path
import tempfile
import unittest

import schedulae
from schedulae.reference_store import MarkdownReferenceStore, parse_references_markdown


class B01IdentityTests(unittest.TestCase):
    def test_package_contains_eleven_domain_modules_and_no_calamus_runtime_module(self):
        package = Path(schedulae.__file__).parent
        domain = {
            "bibliography.py", "bibliography_search.py", "bibtex.py",
            "bibtex_controller.py", "bibtex_import_session.py", "citations.py",
            "reference_controller.py", "reference_store.py", "references.py",
            "related_references.py", "research_file.py",
        }
        self.assertEqual(len(domain), 11)
        self.assertTrue(all((package / name).is_file() for name in domain))
        names = sorted(p.name for p in package.glob("*.py"))
        self.assertFalse(any(name.startswith("calamus_") for name in names))

    def test_runtime_package_has_no_calamus_import_dependency(self):
        package = Path(schedulae.__file__).parent
        for path in package.glob("*.py"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("from calamus_", text, path.name)
            self.assertNotIn("import calamus_", text, path.name)

    def test_all_python_source_and_tests_have_spdx(self):
        root = Path(schedulae.__file__).parent.parent
        for base in (root / "schedulae", root / "tests"):
            for path in base.glob("*.py"):
                text = path.read_text(encoding="utf-8")
                self.assertIn("SPDX-License-Identifier: GPL-3.0-or-later", text, path.name)

    def test_compatibility_header_is_preserved_and_diagnostic_names_it(self):
        records, diagnostics = parse_references_markdown("# Wrong Header\n")
        self.assertEqual(records, ())
        self.assertTrue(diagnostics)
        self.assertEqual(diagnostics[0].message, "Expected library header: # Calamus References v1.")

    def test_no_default_library_path_api_exists(self):
        import schedulae.reference_store as store_module
        self.assertFalse(hasattr(store_module, "default_references_path"))
        signature = inspect.signature(MarkdownReferenceStore)
        self.assertEqual(signature.parameters["path"].default, inspect.Parameter.empty)

    def test_package_import_closure(self):
        modules = (
            "bibliography", "bibliography_search", "bibtex", "bibtex_controller",
            "bibtex_import_session", "citations", "reference_controller",
            "reference_store", "references", "related_references", "research_file",
        )
        for name in modules:
            __import__(f"schedulae.{name}")


if __name__ == "__main__":
    unittest.main()
