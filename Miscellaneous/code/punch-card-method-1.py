# -*- coding: utf-8 -*-
import sys
import numpy
from PIL import Image

#Character set, each hex key is based off the binary representation of the column, not-punched(0) and punched(1)
chars = {0x0:" ",0x1:"&",0x2:"-",0x4:"0",0x8:"1",0x9:"A",0xA:"J",0xC:"/",
         0x10:"2",0x11:"B",0x12:"K",0x14:"S",0x20:"3",0x21:"C",0x22:"L",
         0x24:"T",0x40:"4",0x41:"D",0x42:"M",0x44:"U",0x80:"5",0x81:"E",
         0x82:"N",0x84:"V",0x100:"6",0x101:"F",0x102:"O",0x104:"W",0x200:"7",
         0x201:"G",0x202:"P",0x204:"X",0x400:"8",0x401:"H",0x402:"Q",0x404:"Y",
         0x410:":",0x411:"Ç",0x412:"!",0x420:"#",0x421:".",0x422:"$",0x424:",",
         0x440:"@",0x441:"<",0x442:"*",0x480:">'",0x481:"(",0x482:")",0x484:"_",
         0x500:"=",0x501:"+",0x502:";",0x504:">",0x600:"\"",0x601:"|",0x602:"¬",
         0x604:"?",0x800:"9",0x801:"I",0x802:"R",0x804:"Z"}

#Open image
im = Image.open(sys.argv[1])

#Load image
pix = im.load()

#Create array
data = numpy.chararray((80,12))

#Fill with zeros (not punched)
data.fill("0")

datax = 0
datay = 0

#Primitive "OCR" to detect black blocks
for x in xrange(154,im.size[0]-154,52):
    for y in xrange(168,im.size[1],150):
        if pix[x,y][0] <= 15 and pix[x,y][1] <= 15 and pix[x,y][2] <= 15:                 
            data[datax,datay] = 1
        datay = datay + 1
    datax = datax + 1
    datay = 0

#Loop through the columns, get the binary string, convert to hex, lookup character based on hex key, print character
for col in xrange(0,80):
    binary = "".join(data[col])[::-1]
    hex_s = int(binary, 2)
    sys.stdout.write(chars[hex_s])
