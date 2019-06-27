#!/usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv) < 2:
	print("Usage : %s input-file")
	exit()

im = Image.open(sys.argv[1])

width, height = im.size
pixels = im.load()

# Hardcoded row where the value can be found
gap = [168, 319, 464, 613, 767, 916, 1065, 1226, 1366, 1512, 1663, 1814]

# Based on http://homepage.cs.uiowa.edu/~jones/cards/codes.html
map = {
	"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "11" : "-", "12" : "&",
	"12,1": "A", "12,2": "B", "12,3": "C", "12,4": "D", "12,5": "E", "12,6": "F", "12,7": "G", "12,8": "H", "12,9": "I", "11,1": "J",
	"11,2": "K", "11,3": "L", "11,4": "M", "11,5": "N", "11,6": "O", "11,7": "P", "11,8": "Q", "11,9": "R", "0,1": "/", "0,2": "S", "0,3": "T",
	"0,4": "U", "0,5": "V", "0,6": "W", "0,7": "X", "0,8": "Y", "0,9": "Z", "12,0,1,8,9": "NUL", "11,0,1,8,9": "DS", "": " ", "2,8": ":", "3,8": "#",
	"4,8": "@", "5,8": "'", "6,8": "=", "7,8": "\"", "12,2,8": "[", "12,3,8": ".", "12,4,8": "<", "12,5,8": "(", "12,6,8": "+", "12,7,8": "|",
	"11,2,8": "]", "11,3,8": "$", "11,4,8": "*", "11,5,8": ")", "11,6,8": ";", "11,7,8": "^", "0,2,8": "\\", "0,3,8": ",", "0,4,8": "%",
	"0,5,8": "_", "0,6,8": ">", "0,7,8": "?"
}

res = ""

for x in range(149, 149 + 52*80, 52):
	pos = []
	
	for y in range(12):
		yy = gap[y]
		
		# Slight rework of the index to have them in the order 12, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		y = y - 2 if y >= 2 else 12 - y
		
		if pixels[x, yy][0] == 0 and pixels[x, yy][1] == 0 and pixels[x, yy][2] == 0:
			pos.append(str(y))
		
	key = ",".join(pos)
	
	if key in map:
		res += map[key]
		print(res)
	else:
		res += "(UNKOWN " + key + ")"
