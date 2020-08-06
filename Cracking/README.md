Database
-

* `Keepass` 
	
	* python [code.py](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cracking/code/keepass2john.py) FILE.kdb > crackme
  	* `hashcat -a 0 -m 13400 --show -o out crackme rockyou.txt --force`

Service
-

* `FTP`
	
	* Brute force pasword with known username using [`hydra`](https://tools.kali.org/password-attacks/hydra)
	* `hydra -l <username> -P <wordlist> <target-address> ftp`

* `SSH`
	
	* Brute force pasword with known username using [`hydra`](https://tools.kali.org/password-attacks/hydra)
	* `hydra -t 4 -l jan -P <wordlist> ssh://<target-address>`

ZIP
-

* [`fcrackzip`](http://manpages.ubuntu.com/manpages/trusty/man1/fcrackzip.1.html)

	* Brute force password with dictionary
	* `fcrackzip -v -D -u -p <wordlist> <target.zip>`

* [`zip2john`](https://github.com/magnumripper/JohnTheRipper.git)

	* `zip2john <filename> > crackme`
	* `john crackme --show`

Private key
-

* [`ssh2john`](https://github.com/magnumripper/JohnTheRipper.git)

	* `ssh2john <filename> > crackme`
	* `john crackme --show`
