# SPDX-License-Identifier: GPL-3.0-or-later
"""Native GTK3 application lifecycle for Schedulae."""
from __future__ import annotations

from schedulae.gtk_window import SchedulaeWindow

APPLICATION_ID = "io.github.leviagravia.Schedulae"


def _gtk():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gio, Gtk
    return Gtk, Gio


class SchedulaeApplication:
    def __init__(self) -> None:
        Gtk, Gio = _gtk()
        self.application = Gtk.Application(
            application_id=APPLICATION_ID,
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )
        self.application.connect("activate", self._on_activate)
        self.window: SchedulaeWindow | None = None

    def _on_activate(self, _application) -> None:
        if self.window is None or self.window.disposed:
            self.window = SchedulaeWindow(self.application)
        self.window.present()

    def run(self, argv=None) -> int:
        args = [] if argv is None else list(argv)
        return int(self.application.run(args))


def run(argv=None) -> int:
    return SchedulaeApplication().run(argv)
