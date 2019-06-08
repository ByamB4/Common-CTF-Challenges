#!/usr/bin/env python
import hashlib
import Crypto.Hash.MD4
import re

prefix = '0e'


def breakit():
    iters = 0
    while 1:
        s  = (prefix + str(iters)).encode('utf-8')
        hashed_s = hashlib.new('md4', s).hexdigest()
        
        #print (hashed_s)
        iters = iters + 1
        r = re.match('^0e[0-9]{30}', hashed_s)
        if r:
            print ("[+] found! md5( {} ) ---> {}".format(s, hashed_s))
            print ("[+] in {} iterations".format(iters))
            exit(0)

        if iters % 1000000 == 0:
            print ("[+] current value: {}       {} iterations, continue...".format(s, iters))

breakit()
