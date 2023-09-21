filename = 'changeme.exe'

with open(filename, 'ab') as a, open('kernel32.dll', 'rb') as b:
    a.write(b.read())
