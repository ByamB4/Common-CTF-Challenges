Database cracking
-----------------------

* `Keepass` 
	
	* python [code.py](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cracking/code/keepass2john.py) FILE.kdb > crackme
  	* `hashcat -a 0 -m 13400 --show -o out crackme rockyou.txt --force`

* `FTP` 
	
	* Brute force pasword with known username using `hydra`
	* `hydra -l <username> -P <wordlist> <target address> ftp`
