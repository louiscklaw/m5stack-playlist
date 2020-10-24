#!/usr/bin/env bash

set -ex

cd $REFS/esptool-2.8
  ./esptool.py --port /dev/ttyUSB0 erase_flash
cd ../..