import os

filename = '1760.zip'
os.system('rm -rf python')
os.system('mkdir python')
os.system(f'cp {filename} python')
os.chdir('python')
while True:
    os.system('ls')
    file_com = os.popen(f'file {filename}').read()
    print(f'[+] File: {file_com}')
    if 'Zip archive data,' in file_com:
        print('[+] Zip file')
        password = os.popen(f"fcrackzip -v -u -D -p ../dict.txt {filename}").read().split()[-1]

        print(f'[+] Password: {password}')
        os.popen(f'unzip -P {password} {filename}').read()
        os.system(f'rm {filename}')
        filename = os.popen('ls').read()
    if 'gzip compressed data, was' in file_com:
        print('[+] Gzip file')
        if '.gz' not in filename:
            filename = filename.strip('\n')
            goal = filename + ' ' + filename + '.gz'
            os.system(f'mv {goal}')
            filename += '.gz'
        os.system(f'gzip -d {filename}')
        filename = os.popen('ls').read()
    if 'POSIX tar archive' in file_com:
        print('[+] Tar file')
        os.system(f'tar -xf {filename}')
        os.system(f'rm {filename}')
        filename = os.popen('ls').read()
    else:
        print('[-] Unknown file')
        break
    # input()
