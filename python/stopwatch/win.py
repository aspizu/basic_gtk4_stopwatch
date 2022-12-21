import threading
import time
from datetime import datetime, timedelta

import gi
from headerbar import Headerbar

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GLib, Gtk  # type: ignore


def timefmt(time: timedelta) -> str:
    hours: int = (time.seconds // (60 * 60)) % 60
    mins: int = (time.seconds // 60) % 60
    secs: int = time.seconds % 60
    return f"{hours:02}:{mins:02}:{secs:02}"


class Win(Gtk.ApplicationWindow):
    def __init__(self, app: Gtk.Application):
        super().__init__(title="Stopwatch", application=app)
        self.headerbar = Headerbar()
        self.set_titlebar(self.headerbar)
        self.main_grid = Gtk.Grid()
        self.set_child(self.main_grid)
        self.main_grid.set_halign(Gtk.Align.CENTER)
        self.main_grid.set_valign(Gtk.Align.CENTER)
        self.main_grid.set_margin_top(32)
        self.main_grid.set_margin_bottom(32)
        self.main_grid.set_margin_start(32)
        self.main_grid.set_margin_end(32)
        self.main_grid.set_row_spacing(16)
        self.main_grid.set_column_spacing(16)
        self.time_label = Gtk.Label()
        self.time_label.set_label("Stopped")
        self.time_label.add_css_class("title-1")
        self.start_button = Gtk.Button(label="Start")
        self.start_button.add_css_class("suggested-action")
        self.start_button.connect("clicked", self.start_button_click)
        self.stop_button = Gtk.Button(label="Stop")
        self.stop_button.set_sensitive(False)
        self.stop_button.connect("clicked", self.stop_button_click)
        self.main_grid.attach(self.time_label, 0, 0, 2, 1)
        self.main_grid.attach(self.start_button, 0, 1, 1, 1)
        self.main_grid.attach(self.stop_button, 1, 1, 1, 1)

    def start_button_click(self, widget):
        self.timer_running = threading.Event()

        def timeloop():
            while not self.timer_running.is_set():
                GLib.idle_add(self.update_time_label)
                time.sleep(0.1)

        self.start_time = datetime.now()
        thread = threading.Thread(target=timeloop)
        thread.start()
        self.start_button.set_sensitive(False)
        self.stop_button.set_sensitive(True)
        self.start_button.remove_css_class("suggested-action")

    def update_time_label(self):
        self.end_time = datetime.now()
        diff = self.end_time - self.start_time
        self.time_label.set_label(timefmt(diff))

    def stop_button_click(self, widget):
        self.timer_running.set()
        self.update_time_label()
        self.start_button.set_sensitive(True)
        self.stop_button.set_sensitive(False)
        self.start_button.add_css_class("suggested-action")
