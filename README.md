---
slug: "/m5stack-playlist"
date: "2020-10-24"
title: "my m5stack playlist"
tags: ["m5stack","esp32","micropython"]
---

# m5stack-playlist
![](https://raw.githubusercontent.com/louiscklaw/m5stack-playlist/master/docs/helloworld.png)

m5stack-playlist

### hardware
- display: 320 x 240 pixels


### arduino ide
`aria2c https://downloads.arduino.cc/arduino-1.8.13-linux64.tar.xz`

- `pip install pyserial`
- `pip install esptool`

1. add preferences in arduino ide
- `https://dl.espressif.com/dl/package_esp32_index.json`

tools > board manager > done loading > install esp32

manage library

### vscode
#### micro python
  - building
    - https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/build
  - `cd micropython-esp32/firmware/MicroPython_ESP32_psRAM_LoBo`
  - `BUILD.sh menuconfig`
  - `BUILD.sh clean`
  - `BUILD.sh`
  - `BUILD.sh flash`
  - install extensions `vscode-m5stack-mpy`


### tools
#### to erase m5 stack
- connect usb to computer
- check port generated (e.g. /dev/ttyUSB0)
- on project home, scripts/erase.sh
```
m5stack-playlist on  develop [!?]
➜ scripts/erase.sh
+ cd _ref/esptool-2.8
+ ./esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting........__
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, Coding Scheme None
Crystal is 40MHz
MAC: 30:ae:a4:4f:a3:20
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 13.5s
Hard resetting via RTS pin...
+ cd ../..
```