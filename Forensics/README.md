Forensics
-----------

* Python bytecode `uncompyle6`

	Python гийн compile хийгдсэн файлыг `uncompyle6` ашиглан decompile хийнэ. 

* [Magic Numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files)

	Файл болгонд өөрийн таних тэмдэг болгон Hex утгууд байдаг зарим тохиолдолд тэдгээрийг нь өөрчилсөн байна. Ихэнх файлын гарын үсгийг эндээс харж [болно](https://en.wikipedia.org/wiki/List_of_file_signatures).
	
* [hexed.it](https://hexed.it/)

	Онлайн түүл өгөгдсөн файлын HEX утгуудыг засварлан янзлана.
	
* `foremost`

	Командын мөрний түүл файл дотор нуугдсан файлуудыг ил гаргаж ирнэ.

* `binwalk` 

	Командын мөрний түүл файлд анализ хийхээс гадна нуугдсан файлуудыг гаргаж ирнэ. 
	
```
binwalk -e [FILENAME]
binwalk -D='.*' [FILENAME]
```

* [TestDisk](https://www.cgsecurity.org/Download_and_donate.php/testdisk-7.1-WIP.linux26.tar.bz2)

	Командын мөрний түүл `.dd`, `.img` файлуудаас устсан файлыг сэргээх засварлах юм.
  
PNG File Forensics
--------------------

* `pngcheck`

	Командын мөрний түүл өгөгдсөн `png` файлын бүрэн бүтэн байгаа эсэхийг анализ хийнэ.
  

PDF Files
-------------

* `pdfinfo`	
	
	Командын мөрний түүл ямар төрлийн `pdf` файл вэ зэрэгт анализ хийнэ.

* `pdfcrack`

	Командын мөрний түүл нууц үгээр хамгаалагдсан PDF файлыг `bruteforce`, `dictionary` аас тайлна.
