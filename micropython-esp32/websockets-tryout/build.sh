#!/usr/bin/env bash

set -ex

SRC_DIR=$PWD

# IMG_DIR=$MICRO_PYTHON_BUILD_DIR/components/internalfs_image/image

# cd $MICRO_PYTHON_BUILD_DIR
#   ./BUILD.sh makefs
# cd -

# rsync -avzh \
# $PWD/*.py \
# $IMG_DIR

# # flash to device
# $PWD/../spiffs_image-tryout/test.sh

# code $PWD/main.py

cd $PROJ_HOME
  scripts/0_clean.sh

  # cp $SRC_DIR/sdkconfig $ACTIVE_SDKCONFIG
  # scripts/1_menuconfig.sh

  # restore sdkconfig
  cp  \
    $SRC_DIR/sdkconfig \
    $ACTIVE_SDKCONFIG

  code $ACTIVE_SDKCONFIG

  scripts/2_build_the_firmware.sh

  # sync my code before generate fs image
  rsync -avzh \
    $SRC_DIR/*.py \
    $FS_IMG_DIR

  scripts/3_flash_the_file_system_image.sh
  scripts/4_flash_the_firmware.sh

  # download done, backup the active sdkconfig file
  cp $ACTIVE_SDKCONFIG $SRC_DIR/sdkconfig

  /home/logic/.local/bin/esptool.py run
