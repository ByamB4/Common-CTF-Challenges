Forensics
-----------

* `.wav`

	Нэг төрлийн дууны формат бөгөөд `audacity` түүл ашиглаж болно.
```
Open file -> Straightfire -> Spectrogram
```

* `Python bytecode` uncompyle6

	Python гийн compile хийгдсэн файлыг `uncompyle6` ашиглан decompile хийнэ. 

* [`Magic Numbers`](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files)

	Файл болгонд өөрийн таних тэмдэг болгон Hex утгууд байдаг зарим тохиолдолд тэдгээрийг нь өөрчилсөн байна. Ихэнх файлын гарын үсгийг эндээс харж [болно](https://en.wikipedia.org/wiki/List_of_file_signatures).
	* [https://asecuritysite.com/forensics/magic](https://asecuritysite.com/forensics/magic)
```
PNG -> 	89 50 4e 47 0d 0a 1a 0a
PSD ->  38 42 50 53
```
	
	
* [`hexed.it`](https://hexed.it/)

	Онлайн түүл өгөгдсөн файлын HEX утгуудыг засварлан янзлана.
	
* `foremost`

	Командын мөрний түүл файл дотор нуугдсан файлуудыг ил гаргаж ирнэ.

* `binwalk` 

	Командын мөрний түүл файлд анализ хийхээс гадна нуугдсан файлуудыг гаргаж ирнэ. 
	
```
binwalk -e [FILENAME]
binwalk -D='.*' [FILENAME]
```

* [`TestDisk`](https://www.cgsecurity.org/Download_and_donate.php/testdisk-7.1-WIP.linux26.tar.bz2)

	Командын мөрний түүл `.dd`, `.img` файлуудаас устсан файлыг сэргээх засварлах юм.
