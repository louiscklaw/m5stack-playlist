#!/usr/bin/env bash

set -ex

cd _ref/esptool-2.8
  ./esptool.py --port /dev/ttyUSB0 erase_flash
cd ../..