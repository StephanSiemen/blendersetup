#!/bin/bash

SCRIPT='GlobeTexture_withHeight.py'

BL_FILE='blender-4.2.2-linux-x64.tar.xz'

if [ ! -f ${BL_FILE} ]; then
   echo "Download $BL_FILE ..."
   wget 'https://download.blender.org/release/Blender4.2/blender-4.2.2-linux-x64.tar.xz'
   tar -xf $BL_FILE
fi

blender-4.2.2-linux-x64/blender -b --python ${SCRIPT} -noaudio -E 'CYCLES' -o //render_ -f 1 -F 'PNG'

ls -l .
