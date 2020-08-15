#!/usr/bin/env python

from hashlib import md5
from string import ascii_letters, digits


hashed = '47a37d79305af777742b3074aba9752f'
salt = '1337'

for i in ascii_letters + digits:
    ans = md5(str(i) + salt).hexdigest()  
    print i, ans
    if ans == hashed:
        print 'FOUND'
        print i
        break
print '< END >'
for i in ascii_letters + digits:
    for j in ascii_letters + digits:
        ans = md5(i + j + salt).hexdigest()  
        print i + j, ans
        if ans == hashed:
            print 'FOUND'
            print i
            break
for i in ascii_letters + digits:
    for j in ascii_letters + digits:
        for k in ascii_letters + digits:
            ans = md5(i + j + k + salt).hexdigest()  
            print i + j + k, ans
            if ans == hashed:
                print 'FOUND'
                print i
                break
