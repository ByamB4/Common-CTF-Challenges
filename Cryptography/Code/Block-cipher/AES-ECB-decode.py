from pwn import *
import string

context.log_level = 'error'

def serverTest(p):
  sh = remote('REDACTED', REDACTED)
  # sh = process('REDACTED')

  payload = p
  print(payload)

  sh.sendlineafter(': ', payload)

  data = sh.recvall()

  blocks = []
  for i in range(0, len(data), 32):
    blocks.append(data[i:i+32])
  return blocks

output = 'flag{'
n = 30-15 + len(output)

while True:
  sample = serverTest('a'*10+'a'*(128-n))[12]
  for e in string.printable:
    if e != '\n':
      pass
    if len(output) < 15:
      payload = 'a'*11+'My agent identifying code is: '[-15-15+n:]+output+e
    else:
      payload = 'a'*11+output[-15:]+e
    if serverTest(payload)[4] == sample:
      output += e
      n += 1
      print(output)
      break
