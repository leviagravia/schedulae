#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
LANE_SCRIPT = ROOT / "tools" / "B02_GTK_LANE.py"
LANES = (
    "view-selection",
    "window-shell",
    "library-open",
    "search-filter",
    "new-dialog",
    "edit-duplicate-dialog",
    "delete-dialog",
    "conflict-dialog",
    "malformed-read-only",
    "true-application",
)


def main() -> int:
    print(f"B02_REAL_GTK_LANES={len(LANES)}")
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    current_debug = env.get("G_DEBUG", "")
    env["G_DEBUG"] = ",".join(filter(None, (current_debug, "fatal-criticals")))
    for index, lane in enumerate(LANES, 1):
        print(f"GTK TEST {index}/{len(LANES)} {lane}", flush=True)
        result = subprocess.run(
            [sys.executable, str(LANE_SCRIPT), lane],
            cwd=str(ROOT),
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(result.stdout, end="")
        if result.returncode != 0:
            print("B02_REAL_GTK_RESULT=FAIL")
            print(f"ERR=lane_failed:{lane}:{result.returncode}")
            print("FINAL_PHASE=B02_REAL_GTK_FAIL")
            return result.returncode or 1
    print(f"B02_REAL_GTK_RESULT={len(LANES)}/{len(LANES)}_PASS")
    print("EXIT=0")
    print("ERR=NONE")
    print("FINAL_PHASE=B02_REAL_GTK_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
