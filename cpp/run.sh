#!/bin/bash
set -e

mkdir -p build
cd build
  cmake -DCMAKE_BUILD_TYPE=Debug ../
  make
  clear
  ./src/stopwatch
