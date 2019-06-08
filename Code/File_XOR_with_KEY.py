infile = "chall.png"
outfile = "dec.png"

key = "invisible"

s = open(infile, "r").read()
p = ""
for i in range(len(s)):
	p += chr(ord(s[i]) ^ ord(key[i%len(key)]))

open(outfile, "w").write(p)
