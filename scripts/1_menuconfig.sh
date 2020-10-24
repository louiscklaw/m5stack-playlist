#!/usr/bin/env bash

set -ex

cd $MICRO_PYTHON_BUILD_DIR
  echo './BUILD.sh menuconfig'
  ./BUILD.sh menuconfig
