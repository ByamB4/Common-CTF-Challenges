#!/usr/bin/env python3

import os
import magic
from sys import argv

src = argv[1]
cur = '0'
work = 'work'

print('[+] Creating folder')
os.system(f'rm -rf {work}')
os.mkdir(f'./{work}')
print('[+] Copying file')
os.system(f'cp {src} ./{work}')
os.chdir(f'./{work}')
print('[+] Renaming file')
os.system(f'mv {src} {cur}')


while True:

    file_type = magic.from_file(cur)
    print(f"[+] File {cur}: {file_type}")

    if "7-zip" in file_type:
        os.system(f'7z x {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'POSIX tar archive' in file_type:
        os.system(f'mv {cur} {cur}.tar')
        os.system(f'tar -xf {cur}.tar')
        os.system(f'rm {cur}.tar')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'PPMD archive data' in file_type:
        os.system(f'ppmd d {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'Microsoft Cabinet archive data' in file_type:
        os.system(f'cabextract {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'XZ compressed data' in file_type:
        os.system(f'mv {cur} {cur}.xz')
        os.system(f'xz -d {cur}.xz')
        os.system(f'rm {cur}.xz')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'KGB Archiver' in file_type:
        os.system(f'kgb {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'ARJ archive data' in file_type:
        os.system(f'mv {cur} {cur}.arj')
        os.system(f'arj x {cur}.arj')
        os.system(f'rm {cur}.arj')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'rzip compressed data' in file_type:
        os.system(f'mv {cur} {cur}.rz')
        os.system(f'rzip -d {cur}.rz')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'gzip compressed data' in file_type:
        os.system(f'mv {cur} {cur}.gz')
        os.system(f'gzip -d {cur}.gz')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'Zip archive data' in file_type:
        os.system(f'unzip {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'ARC archive data' in file_type:
        os.system(f'nomarch {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'bzip2 compressed data' in file_type:
        os.system(f'mv {cur} {cur}.bz')
        os.system(f'bunzip2 {cur}.bz')
        os.system(f'rm {cur}.bz')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'Zoo archive data' in file_type:
        os.system(f'mv {cur} {cur}.zoo')
        os.system(f'zoo -extract {cur}.zoo')
        os.system(f'rm {cur}.zoo')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    elif 'RAR archive data' in file_type:
        os.system(f'unrar x {cur}')
        os.system(f'rm {cur}')
        file = os.popen('ls').read().strip()
        cur = str(int(cur) + 1)
        os.system(f'mv {file} {cur}')

    else:
        print('[-] Unknown file')
        break
