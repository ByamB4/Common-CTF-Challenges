### Hash

- `md5`

  - `hashcat -m 0 $(echo '21232f297a57a5a743894a0e4a801fc3') /usr/share/wordlists/rockyou.txt`

- `md5($pass.$salt)`

  - `hashcat -m 10 -a 0 $(echo '5400711cd704e87ed3fd11556cc174ae:SALT') /usr/share/wordlists/rockyou.txt`

- `md5($salt.$pass)`

  - `hashcat -m 20 -a 0 $(echo 'dd679302de4ce83d961f95a1facca536:SALT') /usr/share/wordlists/rockyou.txt`

### Database

- `Keepass`

  - `python [code.py](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cracking/src/keepass2john.py) FILE.kdb > crackme`
    - `hashcat -a 0 -m 13400 --show -o out crackme rockyou.txt --force`

### Service

- `FTP`

  - Brute force pasword with known username using [`hydra`](https://tools.kali.org/password-attacks/hydra)
  - `hydra -l <username> -P <wordlist> <target-address> ftp`

- `SSH`

  - Brute force pasword with known username using [`hydra`](https://tools.kali.org/password-attacks/hydra)
  - `hydra -t 4 -l jan -P <wordlist> ssh://<target-address>`

### ZIP

- [`fcrackzip`](http://manpages.ubuntu.com/manpages/trusty/man1/fcrackzip.1.html)

  - `fcrackzip -v -D -u -p <wordlist> <target.zip>`

- [`zip2john`](https://github.com/magnumripper/JohnTheRipper.git)

  - `./zip2john <filename> > crackme.txt`
  - `./john --wordlist=/usr/share/wordlists/rockyou.txt crackme.txt`
 
- [`zip-crc-cracker`](https://github.com/kmyk/zip-crc-cracker)

  - If file size around 4 byte 

### Web related

- JSON web token hash
 
  - Using `hashcat`
    
    - `echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' > jwt.hash`
    - `hashcat jwt.hash -m 16500 rockyou.txt`

### Private key

- [`ssh2john`](https://github.com/magnumripper/JohnTheRipper.git)

  - `ssh2john <filename> > crackme`
  - `john crackme --show`

### Office

- [`office2john`](https://github.com/magnumripper/JohnTheRipper.git)

  - `./office2john.py ./test.xlsx > crackme.txt`
  - `john --rules --wordlist=rockyou.txt crackme.txt`
  - File extensions:
    - **.ole** CDFV2 Encrypted
    - **.docx**
