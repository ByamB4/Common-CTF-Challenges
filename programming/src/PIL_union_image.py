#!/usr/bin/env python3

from PIL import Image

THE_MAIN = Image.new("RGB", (500, 500), "black")
file = 0

while file < 500:
    image = str(file) + ".png"
    image = Image.open(image)
    THE_MAIN.paste(image, (0, file))
    file += 1
THE_MAIN.save("out.png")
