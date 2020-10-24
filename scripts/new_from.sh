#!/usr/bin/env bash

set -ex

HELLOWORLD_EXAMPLE=$MICRO_PYTHON_EXAMPLE/$1

rsync -avzh --progress $HELLOWORLD_EXAMPLE/ .
