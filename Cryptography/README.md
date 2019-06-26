Cryptography
-----------------------

* `01100010 00110001`

	Битүүдийг тэмдэгтрүү хөрвүүлнэ.
	* [https://www.rapidtables.com/convert/number/binary-to-ascii.html](https://www.rapidtables.com/convert/number/binary-to-ascii.html)
	
* Ихэнх төрлийн transposition cipher дээр ашиглаж болох онлайн түүл. 
	* [https://quipqiup.com/](https://quipqiup.com/)
	* [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

* `Ceaser - 26`

	Англи хэлний 26 үсгэн дотор шилжилт хийж текстээ нууцалж задлана. Rot гэдэг нь хэдэн шилжилт хийснийг илэрхийлнэ. Маш олон онлайн түүл байгаа. Гэвч коммандны мөрнөөс хийвэл илүү амар `caesar` ашиглан (`apt install bsdgames`) аас суулгана. 
	
	```cipher='jeoi{geiwev_gmtliv_ws_svmkmrep}' ; for i in {0..25}; do echo $cipher | caesar $i; done```
	
	* [https://www.dcode.fr/caesar-cipher](https://www.dcode.fr/caesar-cipher)
	* [https://cryptii.com/pipes/caesar-cipher](https://cryptii.com/pipes/caesar-cipher)
	* [https://rot13.com/](https://rot13.com/)
``` 
Svylt Pwzbt pz zptwsf kbttf alea vm aol wypuapun huk afwlzlaapun pukbzayf. Svylt Pwzbt ohz illu aol pukbzayf'z zahukhyk kbttf alea lcly zpujl aol 1500z, dolu hu buruvdu wypualy avvr h nhsslf vm afwl huk zjyhtislk pa av thrl h afwl zwljptlu ivvr. Pa ohz zbycpclk uva vusf mpcl jluabyplz, iba hszv aol slhw puav lsljayvupj afwlzlaapun, ylthpupun lzzluaphssf bujohunlk. Pa dhz wvwbshypzlk pu aol 1960z dpao aol ylslhzl vm Slayhzla zollaz jvuahpupun Svylt Pwzbt whzzhnlz, huk tvyl yljluasf dpao klzravw wbispzopun zvmadhyl sprl Hskbz WhnlThrly pujsbkpun clyzpvuz vm Svylt Pwzbt.
```
	
* `Keyboard шилжилт`

	Keyboard дахь үсэгнүүдийг баруун тийш нь шилжүүлж нууцална.
	* [https://www.dcode.fr/keyboard-shift-cipher](https://www.dcode.fr/keyboard-shift-cipher)
``` 
:ptr, O[di, od do,[;u fi,,u yrcy pg yjr [tomyomh smf yu[rdryyomh omfidytu/ :ptr, O[di, jsd nrrm yjr omfidytu\d dysmfstf fi,,u yrcy rbrt domvr yjr 26--d. ejrm sm imlmpem [tomyrt yppl s hs;;ru pg yu[r smf dvts,n;rf oy yp ,slr s yu[r d[rvo,rm nppl/ Oy jsd ditbobrf mpy pm;u gobr vrmyitord. niy s;dp yjr ;rs[ omyp r;rvytpmov yu[rdryyomh. tr,somomh rddrmyos;;u imvjsmhrf/ Oy esd [p[i;stodrf om yjr 207-d eoyj yjr tr;rsdr pg :rytsdry djrryd vpmysomomh :ptr, O[di, [sddshrd. smf ,ptr trvrmy;u eoyj frdlyp[ [in;odjomh dpgyestr ;olr S;fid {shr<slrt omv;ifomh brtdopmd pg :ptr, O[di,/
```

* `XOR`
	
	Бүх текст XOR үйлдэл хийх боломжтой `\xde\xad\xbe\xef` үүнийг өөрийн компьютер дотроо тайлна гэвэл `pwntools` ашиглаж болно.
```
 python >>> import pwn; pwn.xor("KEY", "RAW_BINARY_CIPHER")
 ```
 
* [`Mnemonic_major_system`](https://en.wikipedia.org/wiki/Mnemonic_major_system)
 
 	Урт тоог цээжлэхийн тулд энэ аргийг ашигладаг бөгөөд үгийг -> тоо, буцаад тоог -> үг хэмээн хувиргана.
	* [https://major-system.info/en/](https://major-system.info/en/)
	* [Python 2 код](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Major_System_Database.py)
```
Pave Pop Poke Pop Dutch Dozen Denim Deism Loot Thatch Pal Atheism Rough Ditch Tonal
```

* `Mobile phone tap code Cipher `

	Олон товчлуурт утсан дээр текст нууцална. Үр дүн нь үргэлж олон дараалсан тоонууд байна.
	* [https://www.dcode.fr/multitap-abc-cipher](https://www.dcode.fr/multitap-abc-cipher)
	
```
6 999 0 7777 88 7 33 777 0 7777 33 222 777 33 8 0 6 33 7777 7777 2 4 33
```


* [`Atbash Cipher`](https://en.wikipedia.org/wiki/Atbash)

	Mapping хийдэг cipher `A` үсгийг `Z` ээр солих гэх `B`-г `Y` солих гэх мэт.
	* [http://rumkin.com/tools/cipher/atbash.php](http://rumkin.com/tools/cipher/atbash.php)
	
* [`Vigenere Cipher`](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

	Түлхүүртэй байх бөгөөд тэр түлхүүрээрээ нууцалж буцааж задалж болно.
	* [https://www.guballa.de/vigenere-solver](https://www.guballa.de/vigenere-solver)
	* [https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)
	* [https://f00l.de/hacking/vigenere.php](https://f00l.de/hacking/vigenere.php)
	
* [`RSA`](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

	Ихэнх тохиолдолд `n`, `c`, `e` өгөгдөх бөгөөд эхлээд [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) ашиглаж үзэх хэрэгтэй. Бусад тохиолдолд гараар бодно.
	* [FactorDB](http://factordb.com/)
	* [IntegerECM](https://www.alpertron.com.ar/ECM.HTM)
	* [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
	* [Python2 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python2.py)
	* [Python3 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python3.py)
	
* `Railfence Cipher`
	
	Симметрик төрлийн түлхүүртэй доош дээшээ шилжинэ.
	* [http://rumkin.com/tools/cipher/railfence.php](http://rumkin.com/tools/cipher/railfence.php)
```
s     e
  e  r  t  => seertc 
    c 
```

* [`Music Sheet Cipher`](https://en.wikipedia.org/wiki/Musical_cryptogram)

	Нотыг ашиглаж өгөгдлөө нууцална.
	* [https://www.dcode.fr/music-sheet-cipher](https://www.dcode.fr/music-sheet-cipher)
	
![`Mortal_theme_score`](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/img/Mortal_theme_score.jpg)

* [`Tupper's Self-Referential Formula`](https://en.wikipedia.org/wiki/Tupper%27s_self-referential_formula)

	x, y байрлалаар дүрс зурна. 
	* [http://keelyhill.github.io/tuppers-formula/](http://keelyhill.github.io/tuppers-formula/)
	
```
960 939 379 918 958 884 971 672 962 127 852 754 715 004 339 660 129 306 651 505 519 271 702 802 395 266 424 689 642 842 174 350 718 121 267 153 782 770 623 355 993 237 280 874 144 307 891 325 963 941 337 723 487 857 735 749 823 926 629 715 517 173 716 995 165 232 890 538 221 612 403 238 855 866 184 013 235 585 136 048 828 693 337 902 491 454 229 288 667 081 096 184 496 091 705 183 454 067 827 731 551 705 405 381 627 380 967 602 565 625 016 981 482 083 418 783 163 849 115 590 225 610 003 652 351 370 343 874 461 848 378 737 238 198 224 849 863 465 033 159 410 054 974 700 593 138 339 226 497 249 461 751 545 728 366 702 369 745 461 014 655 997 933 798 537 483 143 786 841 806 593 422 227 898 388 722 980 000 748 404 719
```
	
![`Tupper decoded image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/img/Tupper's_self_referential_formula_plot.svg)

