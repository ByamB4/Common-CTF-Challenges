# Writen: ByamB4
import os, sys

filename = sys.argv[1]
os.system('rm -rf tmp')
os.system('mkdir tmp')
os.system(f'cp {filename} tmp')
os.chdir('tmp')
while True:
    os.system('ls')
    file_com = os.popen(f'file {filename}').read().split(':')[1]
    print(f'[+] File: {file_com}')
    if 'Zip archive data,' in file_com:
        print('[+] Zip file')
        os.popen(f'unzip {filename}').read()
        os.system(f'rm {filename}')
        filename = os.popen('ls').read()
    elif 'gzip compressed data, was' in file_com:
        print('[+] Gzip file')
        if '.gz' not in filename:
            filename = filename.strip('\n')
            goal = filename + ' ' + filename + '.gz'
            os.system(f'mv {goal}')
            filename += '.gz'
        os.system(f'gzip -d {filename}')
        filename = os.popen('ls').read()
    elif 'POSIX tar archive' in file_com:
        print('[+] Tar file')
        os.system(f'tar -xf {filename}')
        os.system(f'rm {filename}')
        filename = os.popen('ls').read()
    elif 'bzip2' in file_com:
        print('[+] Bzip2 file')
        if '.bzip2' not in filename:
            filename = filename.strip('\n')
            goal = filename + ' ' + filename + '.bzip2'
            os.system(f'mv {goal}')
            filename += '.bzip2'
        os.system(f'bzip2 -d {filename}')
        filename = os.popen('ls').read()
    elif 'XZ compressed data' in file_com:
        print('[+] XZ file')
        if '.xz' not in filename:
            filename = filename.strip('\n')
            goal = filename + ' ' + filename + '.xz'
            os.system(f'mv {goal}')
            filename += '.xz'
        os.system(f'xz -d {filename}')
        filename = os.popen('ls').read()
    # input()
