import gi
from win import Win

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GLib, Gtk  # type: ignore


class App(Adw.Application):
    def __init__(self) -> None:
        super().__init__(
            application_id="io.aspizu.stopwatch", flags=Gio.ApplicationFlags.FLAGS_NONE
        )

    def do_activate(self):
        win = Win(self)
        win.present()
