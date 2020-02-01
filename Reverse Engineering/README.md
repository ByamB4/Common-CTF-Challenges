Reverse engineering
--------------------

* `Stripped binary`

	Stripped буюу хэрэгцээгүй debugging symbol ийг хаясан гэсэн үг. Ингэснээр тухайн програмыг reverse болон disassembly хийхэд хүндрэлтэй болж байгаа юм.
	
	* Тухайн binary файлыг аль санг ашигласныг мэдэж IDA дээрээ нэмж өгнө. [source](https://github.com/maroueneboubakri/lscan/wiki/Reverse-Engineer-a-stripped-binary-with-lscan-and-IDApro)
```
git clone https://github.com/maroueneboubakri/lscan.git
pip install pyelftools pefile
python lscan.py -S amd64/sig -f stripped
cp amd64/sig/libcrypto-1.0.2h.sig ../ida66/sig 
```
	
* `Assembly language`

	Машины хэл дээрх код бөгөөд ойлгож уншиж болно. Зарим үед хэт ойлгомжгүй байвал онлайн түүл ашиглаад diassemble хийгээд ажилуулж болно.
	* [https://defuse.ca/online-x86-assembler.htm#disassembly2](https://defuse.ca/online-x86-assembler.htm#disassembly2) дараа нь **hex** хуулж авч доорх кодонд орлуулж бодож болно.
	
```C
char shellcode[] = "\x55\x89\xE5\xB8\x19\x00\x00\x00\x30\xC0\x8A\x65\x0A\x66\xC1\xE0\x10\x2A\x45\x0D\x02\x65\x0C\x66\x33\x45\x12\x89\xEC\x5D\xC3";

int main(int argc, char **argv){
        int (*fp) (int, int, int);
        fp = (void *)shellcode;
        int ret = fp(0xb5e8e971,0xc6b58a95,0xe20737e9);
        printf("ret = 0x%x\n", ret);

}
// gcc asm3.c -o asm3_out -fno-stack-protector -z execstack -no-pie -m32
```

* `Test2`

