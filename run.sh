#!/bin/bash

SCRIPT = 'GlobeTexture_withHeight.py'
FILE   = 'blender-2.93.4-linux-x64.tar.xz'

LOC = 'blendersetup'

if [ ! -f $FILE]; then
   echo "Download $FILE ..."
   wget 'https://download.blender.org/release/Blender2.93/blender-2.93.4-linux-x64.tar.xz'
   tar -xf $FILE
fi

blender-2.93.4-linux-x64/blender -b --python ${LOC}/${SCRIPT} -noaudio -E 'CYCLES' -f 1 -F 'PNG'
 