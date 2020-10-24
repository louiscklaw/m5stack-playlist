#!/usr/bin/env bash

set -ex

cd $MICRO_PYTHON_BUILD_DIR
  ./BUILD.sh makefs -j16
cd ../../..

cd $MICRO_PYTHON_BUILD_DIR
  ./BUILD.sh flashfs
cd ../../..
