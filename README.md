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


### Logs:

```
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

```
➜ ./BUILD.sh flash

---------------------
MicroPython for ESP32
---------------------

=========================================
Flashing MicroPython firmware to ESP32...
=========================================
Building partitions from /home/logic/_workspace/m5stack-playlist/micropython-esp32/_firmware/MicroPython_BUILD/partitions_mpy.csv...
Flashing binaries to serial port /dev/ttyUSB0 (app at offset 0x10000 )...
esptool.py v2.5.0
Serial port /dev/ttyUSB0
Connecting.....
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core
MAC: 30:ae:a4:4f:a3:20
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 921600
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 19408 bytes to 11547...
Wrote 19408 bytes (11547 compressed) at 0x00001000 in 0.2 seconds (effective 1010.4 kbit/s)...
Hash of data verified.
Compressed 144 bytes to 69...
Wrote 144 bytes (69 compressed) at 0x0000f000 in 0.0 seconds (effective 531.8 kbit/s)...
Hash of data verified.
Compressed 1443456 bytes to 876077...
Wrote 1443456 bytes (876077 compressed) at 0x00010000 in 12.0 seconds (effective 959.8 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 128...
Wrote 3072 bytes (128 compressed) at 0x00008000 in 0.0 seconds (effective 9241.5 kbit/s)...
Hash of data verified.

Leaving...
Staying in bootloader.
OK.
```

### to run helloworld example:
```
# manually reset module

cd /home/logic/_workspace/m5stack-playlist/micropython-esp32/helloworld-tryout
  ./build.sh
```

### TODO:
  - [*] helloworld
  - [] LCD
  - []  Button
  - []  SD Card
  - []  Speaker
  - []  GPIO
  - []  PWM
  - []  ADC
  - []  DAC
  - []  I2C
  - []  SPI
  - []  UART
  - []  Timer
  - []  Neopixel
  - []  RTC
