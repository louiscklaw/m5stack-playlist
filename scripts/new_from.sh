#!/usr/bin/env bash

set -ex

PROJ_NAME=$1

cd micropython-esp32
  mkdir -p $PROJ_NAME
  rsync -avzh --progress helloworld-tryout/ $PROJ_NAME
cd ..
