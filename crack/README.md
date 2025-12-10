# Cracking

Offline/online password recovery cheats: hashes, captures, archives, and services.

## Quick wins
- Try the right hashcat mode first; avoid wasting time on the wrong format.
- Convert captures to crackable hashes (cap2hashcat, zip2john, ssh2john, office2john).
- Keep wordlists handy (`rockyou.txt`, custom event lists).

## Hashes
- MD5: `hashcat -m 0 21232f297a57a5a743894a0e4a801fc3 /usr/share/wordlists/rockyou.txt`
- MD5(pass.salt): `hashcat -m 10 -a 0 '5400711cd704e87ed3fd11556cc174ae:SALT' /usr/share/wordlists/rockyou.txt`
- MD5(salt.pass): `hashcat -m 20 -a 0 'dd679302de4ce83d961f95a1facca536:SALT' /usr/share/wordlists/rockyou.txt`
- GPP CPassword: `python3 gpp-decrypt.py -c PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw`

## Wi-Fi captures
- Convert capture: https://hashcat.net/cap2hashcat/
- Crack WPA handshakes: `hashcat -m 22000 capture.hc22000 rockyou.txt`

## Databases
- KeePass with John:
  ```
  keepass2john database.kdbx > crack.hash
  john crack.hash --format=keepass --wordlist=rockyou.txt
  ```
- KeePass with hashcat:
  ```
  hashcat -a 0 -m 13400 --show -o out crackme.kdbx rockyou.txt --force
  ```

## Services
- FTP brute (known user): `hydra -l <user> -P <wordlist> <target> ftp`
- SSH brute (known user): `hydra -t 4 -l jan -P <wordlist> ssh://<target>`

## Archives (ZIP)
- Dictionary: `fcrackzip -v -D -u -p <wordlist> target.zip`
- John route:
  ```
  zip2john target.zip > crackme.txt
  john --wordlist=/usr/share/wordlists/rockyou.txt crackme.txt
  ```
- Known plaintext attack: https://github.com/kimci86/bkcrack
- CRC short files: https://github.com/kmyk/zip-crc-cracker (useful if file size ~4 bytes)

## Web/JWT
- JWT HS256 with hashcat:
  ```
  echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' > jwt.hash
  hashcat jwt.hash -m 16500 rockyou.txt
  ```

## PDFs
- `pdfcrack --wordlist=rockyou.txt crackme.pdf`

## Private keys
- SSH private key: `ssh2john id_rsa > crackme && john crackme --show`

## Office docs
- `office2john.py test.xlsx > crackme.txt`
- `john --rules --wordlist=rockyou.txt crackme.txt`
- Common extensions: `.ole` (CDFV2), `.docx`, `.xlsx`
