#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import time
START = time.perf_counter()
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
from schedulae.gtk_app import SchedulaeApplication

wrapper = SchedulaeApplication()
state = {"mapped": False}


def on_window_added(_app, window):
    def on_map(_window, _event):
        if not state["mapped"]:
            state["mapped"] = True
            elapsed = (time.perf_counter() - START) * 1000.0
            print(f"FIRST_MAPPED_MS={elapsed:.3f}", flush=True)
            GLib.idle_add(wrapper.application.quit)
        return False
    window.connect("map-event", on_map)


wrapper.application.connect("window-added", on_window_added)
rc = wrapper.run([sys.argv[0]])
if not state["mapped"]:
    print("STARTUP_METRIC=FAIL")
    raise SystemExit(1)
print("STARTUP_METRIC=PASS")
raise SystemExit(rc)
