#!/usr/bin/env bash


set -ex

cd micropython-esp32/_firmware/MicroPython_BUILD
  ./BUILD.sh flashfatfs

cd -
