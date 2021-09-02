#!/bin/bash

#
# prereq on CentOS: 
#     sudo yum install libX11 libXi libXrender libXxf86vm libXfixes
#

SCRIPT='GlobeTexture_withHeight.py'

BL_FILE='blender-2.93.4-linux-x64.tar.xz'

LOC='blendersetup'

if [ ! -f $BL_FILE]; then
   echo "Download $BL_FILE ..."
   wget 'https://download.blender.org/release/Blender2.93/blender-2.93.4-linux-x64.tar.xz'
   tar -xf $BL_FILE
fi

blender-2.93.4-linux-x64/blender -b --python ${LOC}/${SCRIPT} -noaudio -E 'CYCLES' -f 1 -F 'PNG'
