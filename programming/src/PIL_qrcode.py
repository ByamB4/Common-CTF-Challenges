#!/usr/bin/env python3

from PIL import Image

im = Image.open("1.png").convert("RGB")

newimgdata = []

for i in im.getdata():
    # print(i)
    if i == (216, 222, 233):
        newimgdata.append((255, 255, 255))
    else:
        newimgdata.append((0, 0, 0))
newim = Image.new(im.mode, im.size)
newim.putdata(newimgdata)
newim.save("out.png")
