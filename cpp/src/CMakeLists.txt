link_directories(${GTKMM_LIBRARY_DIRS})
include_directories(${GTKMM_INCLUDE_DIRS})
add_executable(stopwatch main.cpp)
target_link_libraries(stopwatch ${GTKMM_LIBRARIES})
