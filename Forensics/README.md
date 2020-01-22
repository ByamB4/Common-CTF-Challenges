Forensics
-----------

* `Нуугдсан файл`
	* `foremost` файл дотор нуугдсан файлуудыг ил гаргаж ирнэ.
	* `binwalk` файлд анализ хийхээс гадна нуугдсан файлуудыг гаргаж ирнэ.
	
* `Reverse HEX`

	* Заримдаа файлын hex утгууд ямар ч замбараагүй байдалтай өгөгдөх бөгөөд үүнийг python ашиглаж reverse хийнэ.
	* `open('output2.txt', 'wb').write(open('output.txt', 'rb').read()[::-1])`

* `Python bytecode`

	* Python гийн compile хийгдсэн файлыг `uncompyle6` ашиглан decompile хийнэ. 
	

* `TestDisk`

	* Командын мөрний түүл `.dd`, `.img` файлуудаас устсан файлыг сэргээх засварлах юм.


PNG File Forensics
--------------------

* `Magic Numbers`

	* [default-image-1](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Forensics/Files/png-default.png) 
	* PNG файл засна [png-parser](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Forensics/Code/png_parser.py)
	
* `pngcheck`

	* Командын мөрний түүл өгөгдсөн `png` файлын бүрэн бүтэн байгаа эсэхийг анализ хийнэ.
	
* `2 ижил зураг`

	* 2 ижилхэн зураг гарч ирвэл SUB,OR, XOR, MUL гэх мэт үйлдэл хийж нэг зураг болгож нэгтгэх.
		* `compare 00000000.png 00000725.png -compose src diff.png`
	
PDF Files
-------------

* `pdfinfo`	
	
	* Командын мөрний түүл ямар төрлийн `pdf` файл вэ зэрэгт анализ хийнэ.
	
* `pdf2txt`
	
	* Python файл `.pdf` файлуудаас текст гарган авна.
		* [https://github.com/euske/pdfminer](https://github.com/euske/pdfminer)

* `pdfcrack`

	* Командын мөрний түүл нууц үгээр хамгаалагдсан PDF файлыг `bruteforce`, `dictionary` аас тайлна.

* `pdf-repair`

	* Онлайн түүл pdf файлыг засна.
		* [https://www.pdf-online.com/osa/repair.aspx](https://www.pdf-online.com/osa/repair.aspx)

* `pdf-parser`

	Kali-linux командын мөрний түүл.

ZIP File Forensics
--------------------

* [`fcrackzip` ](https://allanfeid.com/content/cracking-zip-files-fcrackzip)

	Командын мөрний түүл `.zip` файлуудыг brute-force ийн аргаар тайлна. Ихэнх тохиолдолд dictionary нь [`rockyou.txt`](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) байх боловч зарим тохиолдолд өөр файлтай цуг өгөгдөн тэр файлаас dictionary гаргаж авна.
```
fcrackzip -v -D -u -p /usr/share/dict/words secret.zip
```

* `Too many zipped`

	Ихэнх даалгаврууд дээр маш олон удаа шахсан байдалтай орж ирэх юм. Үүнийг одоогийн байдлаар ямар бэлэн түүл олоогүй ихэнх тохиолдолд гараар бичиж байгаа. 
	* [Нэг төрлийн ZIP](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/ZIP/code/crack-1.py)

* `strings` 

	Зарим zip файл нэг файлтай хамт өгөгдөх бөгөөд мэдээж нууц үгтэй байвал тэр хамт ирсэн файл нь dictionary байх боломжтой юм. 
	`strings [FILENAME] > dict.txt`

* `ZIP password produce flag`

	TJCTF дээр иймэрхүү даалгавар ирж байсан ба маш олон .zip файлуудын нууц үг нь манай флагийг гаргаж ирж байсан.
	* [bash-script](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/ZIP/code/unzip-withbruteforce-files.sh)
	
RAR File Forensics
--------------------

* `Password protected`

	rar2john ашиглаж hash ийн гаргаж аваад дараа нь wordlist ээр brute force хийнэ.
	* `rar2john [NAME].rar > rar.hash`
	* `john --wordlist /usr/share/wordlists/rockyou.txt --format=rar5 rar.hash`
	
GIF File Forensics
--------------------

* `gif split`

	`GIF` зургийг салгаж нэгтгэн ганц зураг гаргана.
	* `convert test.gif %02d.png`
	* `ls *.png | while read filename; do convert $filename -transparent white $filename; done`
	* `ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done`
	
WAV File Forensics
--------------------

* `SSTV audio file to image using QSSTV`
	
	
