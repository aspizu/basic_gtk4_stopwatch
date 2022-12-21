#include <gtkmm.h>
#include "app.cpp"
#include "win.cpp"


int main(int argc, char** argv) {
  auto app = App::create("io.aspizu.stopwatch");
  return app->make_window_and_run<Win>(argc, argv);
}
