#!/usr/bin/python
# Writen l3yam134

import pwn 

f = open('[IN FILE NAME]', 'r').read()
open('[OUT FILE NAME]', 'w').write(pwn.xor(f, '[YOUR KEY]'))
