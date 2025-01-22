#!/bin/sh

sdptool add --channel=2 SP
mknod /dev/rfcomm0 c 216 0
rfcomm listen 0 2
