#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import ast
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
PKG = ROOT / "schedulae"
TESTS = ROOT / "tests"
TOOLS = ROOT / "tools"

DOMAIN = {
    "bibliography.py", "bibliography_search.py", "bibtex.py", "bibtex_controller.py",
    "bibtex_import_session.py", "citations.py", "reference_controller.py",
    "reference_store.py", "references.py", "related_references.py", "research_file.py",
}
SHELL = {"gtk_app.py", "gtk_window.py", "gtk_reference_view.py", "gtk_dialogs.py", "__main__.py"}
ALLOWED_TOP_IMPORTS = set(sys.stdlib_module_names) | {"schedulae", "gi", "__future__"}


def fail(code: int, message: str):
    print("B02_SOURCE_VERIFY=FAIL")
    print(f"ERR={message}")
    print(f"EXIT={code}")
    print("FINAL_PHASE=B02_SOURCE_VERIFY_FAIL")
    raise SystemExit(code)


if not PKG.is_dir() or not TESTS.is_dir() or not TOOLS.is_dir():
    fail(2, "missing_source_topology")

py_names = {p.name for p in PKG.glob("*.py")}
if not DOMAIN.issubset(py_names):
    fail(3, f"missing_domain:{sorted(DOMAIN-py_names)}")
if not SHELL.issubset(py_names):
    fail(4, f"missing_shell:{sorted(SHELL-py_names)}")
if len(DOMAIN) != 11 or len(SHELL) != 5:
    fail(5, "internal_expected_topology")
if any(name.startswith("calamus_") for name in py_names):
    fail(6, "calamus_runtime_module")

for name in DOMAIN:
    text = (PKG / name).read_text(encoding="utf-8")
    if "import gi" in text or "from gi" in text:
        fail(7, f"gtk_import_in_domain:{name}")

runtime_calamus = []
for path in PKG.glob("*.py"):
    text = path.read_text(encoding="utf-8")
    if "from calamus_" in text or "import calamus_" in text:
        fail(8, f"calamus_import:{path.name}")
    for lineno, line in enumerate(text.splitlines(), 1):
        if "Calamus" in line:
            runtime_calamus.append((path.name, lineno, line.strip()))
if runtime_calamus != [("reference_store.py", 13, '_HEADER = "# Calamus References v1"')]:
    fail(9, f"unexpected_calamus_runtime_strings:{runtime_calamus}")

for base in (PKG, TESTS, TOOLS):
    for path in base.glob("*.py"):
        text = path.read_text(encoding="utf-8")
        if "SPDX-License-Identifier: GPL-3.0-or-later" not in text:
            fail(10, f"missing_spdx:{path.relative_to(ROOT)}")
        try:
            tree = ast.parse(text, filename=str(path))
        except SyntaxError as error:
            fail(11, f"syntax:{path.name}:{error}")
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots = [alias.name.split(".", 1)[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                roots = [node.module.split(".", 1)[0]]
            else:
                continue
            for root in roots:
                if root not in ALLOWED_TOP_IMPORTS:
                    fail(12, f"third_party_or_unknown_import:{path.name}:{root}")

shell_text = "\n".join((PKG / name).read_text(encoding="utf-8") for name in SHELL)
for forbidden in ("Gtk.events_pending", "main_iteration", "scroll_to_cell", "grab_focus"):
    if forbidden in shell_text:
        fail(13, f"forbidden_lifecycle_pattern:{forbidden}")
if 'self.search_entry.connect("search-changed", self._on_search_changed)' in shell_text:
    fail(17, "search_signal_double_debounce")
if 'self.search_entry.connect("changed", self._on_search_changed)' not in shell_text:
    fail(18, "search_signal_changed_missing")
lane_text = (ROOT / "tools" / "B02_GTK_LANE.py").read_text(encoding="utf-8")
search_start = lane_text.find("def lane_search_filter() -> int:")
search_end = lane_text.find("\n\ndef lane_new_dialog() -> int:", search_start)
if search_start < 0 or search_end < 0:
    fail(19, "search_filter_lane_missing")
search_lane = lane_text[search_start:search_end]
if "GLib.timeout_add(260, check)" in search_lane:
    fail(20, "search_filter_fixed_time_oracle")
for required in (
    "deadline = time.monotonic() +",
    "delivery_count",
    "last_delivered_query",
    "not shell._search_dispatcher.pending",
    'shell.controller.filters.query == "alpha"',
    "poll_semantic_completion",
):
    if required not in search_lane:
        fail(21, f"search_filter_bounded_oracle_missing:{required}")
for forbidden in ("Import BibTeX", "Export BibTeX", "Toolbar", "Gtk.Toolbar"):
    if forbidden in shell_text:
        fail(14, f"b02_scope_leak:{forbidden}")

identity = (ROOT / "PROJECT_IDENTITY.toml").read_text(encoding="utf-8")
for needle in (
    'future_desktop_app_id = "io.github.leviagravia.Schedulae"',
    'b02_application_id = "io.github.leviagravia.Schedulae"',
    'b02_gtk_stack = "GTK3-PyGObject"',
    'b02_candidate = false',
):
    if needle not in identity:
        fail(15, f"identity_missing:{needle}")

main_text = (PKG / "__main__.py").read_text(encoding="utf-8")
if "from schedulae.gtk_app import run" not in main_text:
    fail(16, "main_entrypoint")

print("B02_SOURCE_VERIFY=PASS")
print("DOMAIN_MODULES=11")
print("SHELL_MODULES=5")
print("PYTHON_NAMESPACE=schedulae")
print("DOMAIN_GTK_IMPORTS=0")
print("SHELL_GTK_STACK=GTK3_PYGOBJECT")
print("INTENTIONAL_CALAMUS_RUNTIME_STRINGS=1")
print("COMPATIBILITY_HEADER=# Calamus References v1")
print("APPLICATION_ID=io.github.leviagravia.Schedulae")
print("THIRD_PARTY_RUNTIME_DEPS=PyGObject_ONLY")
print("TOOLBAR=NO")
print("IMPORT_EXPORT_UI=NO")
print("EXPECTED_HEADLESS_TESTS=131")
print("EXPECTED_REAL_GTK_LANES=10")
print("BYTECODE_ARTIFACTS=0")
print("EXIT=0")
print("ERR=NONE")
print("FINAL_PHASE=B02_SOURCE_VERIFY_PASS")
