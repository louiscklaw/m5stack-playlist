#!/usr/bin/env bash

set -ex

IMG_DIR=$MICRO_PYTHON_BUILD_DIR/components/internalfs_image/image

$MICRO_PYTHON_BUILD_DIR/BUILD.sh makefs

rsync -avzh \
$PWD/*.py \
$IMG_DIR

# flash to device
$PROJ_HOME/scripts/erase.sh
$PWD/../spiffs_image-tryout/test.sh

code $PWD/main.py
