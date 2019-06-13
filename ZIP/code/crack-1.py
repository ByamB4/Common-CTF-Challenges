#!/usr/bin/python3

import os, re

file = '49805.zip'
while True:
	print('[*] Unzipping : ' + file)
	pwd = os.popen('strings ' + file).read().split('\n')[-2][:-6]
	os.system('unzip -P ' + pwd + ' ' + file)
	file = pwd + '.zip'
