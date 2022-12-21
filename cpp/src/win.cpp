#include <iostream>
#include <gtkmm.h>
#include "headerbar.cpp"
#include "timerworker.cpp"

class Win: public Gtk::ApplicationWindow {
  public:
  HeaderBar   headerbar    = HeaderBar();
  Gtk::Grid   main_grid    = Gtk::Grid();
  Gtk::Label  time_label   = Gtk::Label();
  Gtk::Button start_button = Gtk::Button();
  Gtk::Button stop_button  = Gtk::Button();

  Win() {
    set_title("Stopwatch");
    set_default_size(200, 200);
    set_titlebar(headerbar);
    set_child(main_grid);
    main_grid.set_halign(Gtk::Align::CENTER);
    main_grid.set_valign(Gtk::Align::CENTER);
    main_grid.set_margin_top(32);
    main_grid.set_margin_bottom(32);
    main_grid.set_margin_start(32);
    main_grid.set_margin_end(32);
    main_grid.set_row_spacing(16);
    main_grid.set_column_spacing(16);
    time_label.set_label("Stopped");
    time_label.add_css_class("title-1");
    start_button.set_label("Start");
    start_button.add_css_class("suggested-action");
    start_button.signal_clicked().connect(
      sigc::mem_fun(*this, &Win::start_button_onclick)
    );
    stop_button.set_label("Stop");
    stop_button.signal_clicked().connect(
      sigc::mem_fun(*this, &Win::stop_button_onclick)
    );
    stop_button.set_sensitive(false);
    main_grid.attach(time_label, 0, 0, 2, 1);
    main_grid.attach(start_button, 0, 1, 1, 1);
    main_grid.attach(stop_button, 1, 1, 1, 1);
  }

  void start_button_onclick() {
    start_button.set_sensitive(false);
    start_button.remove_css_class("suggested-action");
    stop_button.set_sensitive(true);
  }

  void stop_button_onclick() {
    start_button.set_sensitive(true);
    start_button.add_css_class("suggested-action");
    stop_button.set_sensitive(false);
  }
};
