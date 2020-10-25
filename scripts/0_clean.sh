#!/usr/bin/env bash

set -ex

cd $MICRO_PYTHON_BUILD_DIR

  git clean -dfx
  git reset --hard

  # ./BUILD.sh clean
