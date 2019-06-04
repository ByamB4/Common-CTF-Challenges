#!/usr/bin/python
# Writen l3yam134
from pwn import *
import string

s = remote('crypto.hsctf.com', 8111)

print s.recv()

cipherText = s.recv()
cipherText = str([text for text in cipherText.split() if len(text) == 106])
print '[+] Cipher text : %s' % cipherText
send = 'hsctf{'
s.sendline(send)

flag = s.recv()
wordList = string.ascii_letters + string.digits + '_!@#}?'
length = 14

print '======================================'

print flag.split(' ')[1]

while True:
    for i in wordList:
        s.sendline(send + i)
        print '[+] Sending %s' % send + i
        received = s.recv()
        received = received.split()[1]
        # print '[+] Received %s' % received
        check = cipherText[:length + 2]
        # print '[+] Comparing : {0} == {1}'.format(received, check[2:])
        if received == check[2:]:
            # print '[+] Nice'
            length += 2
            send += wordList[wordList.index(i) - 1]
            # raw_input()
