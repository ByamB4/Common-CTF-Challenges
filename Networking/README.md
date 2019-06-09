Networking
---------------

* [Wireshark](https://www.wireshark.org/)

	`.pcap` файлууд дээр анализ хийнэ.

* [Network Miner](http://www.netresec.com/?page=NetworkMiner)

	`.pcap` болон `.pcapng` файлууд дээр анализ хийнэ.
	
* [`.pcapng`](https://github.com/pcapng/pcapng)

	Ихэнх файл ийм байгаад байдаггүй гэхдээ хувиргах шаардлага гарвал
	* [http://pcapng.com/](http://pcapng.com/)
	
* [`tcpflow`][tcpflow]

	Командын мөрний түүл `.pcap` файлаас нуугдсан файл илрүүлнэ. 
```
tcpflow -r my_file.pcap
ls -1t | head -5 # see the last 5 recently modified files
```
