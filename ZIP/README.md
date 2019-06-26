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
