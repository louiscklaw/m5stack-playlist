#!/usr/bin/env bash

set -ex

curl -i -N -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Host: echo.websocket.org" -H "Origin: https://www.websocket.org" https://echo.websocket.org
