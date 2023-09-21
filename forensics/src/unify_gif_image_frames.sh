#!/bin/bash

# convert [img].gif %02d.png
ls *.png | while read filename; do convert $filename -transparent white $filename;  done
ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done
