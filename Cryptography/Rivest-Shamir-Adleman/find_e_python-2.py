#!/usr/bin/env python

from Crypto.Util.number import inverse

n=1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139

# P and Q found on http://factordb.com/

p=37975227936943673922808872755445627854565536638199
q=40094690950920881030683735292761468389214899724061

c=823987601539551928252661654437667295378450335918666145079851234798343062080579451801129289418220555

phi=(p-1)*(q-1)

# We search e

for e in range(65537):
  d = inverse(e, phi)
  m = pow(c, d, n)
  try:
    uncipher = hex(m)[2:-1].decode('hex')
  except:
    continue
  if uncipher[:8] == 'InnoCTF{':
    print '[*] Found : %s' % e 
    print '[+] %s ' % uncipher
    raw_input()
  print '[+] %s ' % e
