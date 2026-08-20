#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import os
from pathlib import Path
import re
import statistics
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from schedulae.bibliography import BibliographyFilters, build_bibliography_context, project_references
from schedulae.gtk_reference_view import projection_rows
from schedulae.references import ReferenceRecord

SAMPLES = 5


def main() -> int:
    env = os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"] = "1"
    values = []
    script = ROOT / "tools" / "B02_STARTUP_METRIC.py"
    for i in range(1, SAMPLES + 1):
        result = subprocess.run(
            [sys.executable, str(script)], cwd=str(ROOT), env=env,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        print(f"STARTUP SAMPLE {i}/{SAMPLES}")
        print(result.stdout, end="")
        if result.returncode != 0:
            print("B02_PERF_PROBE=FAIL")
            print(f"ERR=startup_sample:{i}:{result.returncode}")
            print("FINAL_PHASE=B02_PERF_PROBE_FAIL")
            return result.returncode or 1
        match = re.search(r"FIRST_MAPPED_MS=([0-9.]+)", result.stdout)
        if not match:
            print("B02_PERF_PROBE=FAIL"); print("ERR=missing_startup_metric"); return 2
        values.append(float(match.group(1)))

    records = tuple(
        ReferenceRecord(
            key=f"author2026title{i}", title=f"Title {i}", type="article" if i % 2 else "book",
            authors=(f"Author {i % 50}",), year=str(2000 + i % 27), tags=(f"tag{i % 20}",),
        )
        for i in range(1000)
    )
    context = build_bibliography_context(records)
    t0 = time.perf_counter(); rows = projection_rows(records, context); projection_ms = (time.perf_counter() - t0) * 1000.0
    t0 = time.perf_counter(); result = project_references(records, BibliographyFilters(query="Title 999"), context); search_ms = (time.perf_counter() - t0) * 1000.0
    if len(rows) != 1000 or len(result) != 1:
        print("B02_PERF_PROBE=FAIL"); print("ERR=projection_or_search_result"); return 3

    print(f"STARTUP_SAMPLES={SAMPLES}")
    print(f"STARTUP_FIRST_MAPPED_MIN_MS={min(values):.3f}")
    print(f"STARTUP_FIRST_MAPPED_MEDIAN_MS={statistics.median(values):.3f}")
    print(f"STARTUP_FIRST_MAPPED_MAX_MS={max(values):.3f}")
    print(f"PROJECTION_1000_MS={projection_ms:.3f}")
    print(f"SEARCH_1000_MS={search_ms:.3f}")
    print("THRESHOLD_GATE=NOT_FROZEN_NONCANDIDATE_MEASUREMENT_ONLY")
    print("B02_PERF_PROBE=PASS")
    print("EXIT=0")
    print("ERR=NONE")
    print("FINAL_PHASE=B02_PERF_PROBE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
