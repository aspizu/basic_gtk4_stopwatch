import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GLib, Gtk  # type: ignore


class Headerbar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()
