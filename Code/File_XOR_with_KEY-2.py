def xor(data,key):
	l=len(key)
	return bytearray(((data[i] ^ key [i%l]) for i in range(0,len(data))))


data = bytearray(open('chall.png','rb').read())
key= bytearray([0x69,0x6e,0x76,0x69,0x73,0x69,0x62,0x6c,0x65])

a = xor(data,key)

f = open('my_file','w+b')
f.write(a)
f.close()
