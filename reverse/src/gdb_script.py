#!/usr/bin/env python3
# use plain gdb
# gdb -q -x x.py
import gdb
from string import *

gdb.execute('set pagination off')
gdb.execute('set confirm off')
gdb.execute('file checker')
gdb.execute('b *main+170')

letters = '_' + digits + ascii_letters + '{}'

flag = ''
for i in range(49):
    for j in letters:
        user_input = flag + j
        gdb.execute(f"r <<< {user_input}")

        for k in range(len(flag)):
            gdb.execute(f"x/gx $rdi", to_string=True).split("\t")[-1].replace('\n', '')
            gdb.execute(f"x/gx $rsi", to_string=True).split("\t")[-1].replace('\n', '')
            gdb.execute('c')

        a = gdb.execute(f"x/gx $rdi", to_string=True).split("\t")[-1].replace('\n', '')
        b = gdb.execute(f"x/gx $rsi", to_string=True).split("\t")[-1].replace('\n', '')
        
        print('a', a)
        print('b', b)

        print(f'[{len(flag)}]', j)

        if a == b:
            flag += j
            print('[found]', flag)
            input('continue?')
            break
