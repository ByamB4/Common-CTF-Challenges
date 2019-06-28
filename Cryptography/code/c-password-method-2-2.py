#!/usr/bin/env python2

# I Lost my password can you find it? - 3 points
'''
You get the archive, unpack it and search for password:
    tar xf d22fdb09ef96576dfc49076a9322a555.tar
    cd Policies
    grep -R password *
You get an XML file attribute:
    cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
This is our password. Now google "cpassword policies":
    https://blogs.technet.microsoft.com/ash/2014/11/10/dont-set-or-save-passwords-using-group-policy-preferences/
    https://adsecurity.org/?p=2288
    https://msdn.microsoft.com/en-us/library/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be.aspx
     - get the 32-byte AES key
'''
import base64
from Crypto.Cipher import AES

# base64 encoded with missing padding
cpassword = 'PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw'
# add the missing padding
missing_padding = 4 - len(cpassword) % 4
cpassword = cpassword + '=' * missing_padding

# key from web
key_string = "4e 99 06 e8 fc b6 6c c9 fa f4 93 10 62 0f fe e8 f4 96 e8 06 cc 05 79 90 20 9b 09 a4 33 b6 6c 1b"
key = ''.join(key_string.split(" "))
key = key.decode('hex')

# default iv and init key
iv = '\x00'*AES.block_size
aes = AES.new(key, AES.MODE_CBC, iv)

passwd = aes.decrypt(base64.b64decode(cpassword))

print passwd.strip()
