#!/usr/bin/env bash

set -ex

rsync -avzh \
micropython-esp32/LCD-tryout/main.py \
micropython-esp32/_firmware/MicroPython_BUILD/components/internalfs_image/image/main.py

micropython-esp32/spiffs_image-tryout/test.sh
