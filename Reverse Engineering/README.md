Reverse engineering
--------------------

* `Assembly language`

	Машины хэл дээрх код бөгөөд ойлгож уншиж болно. Зарим үед хэт ойлгомжгүй байвал онлайн түүл ашиглаад diassemble хийгээд ажилуулж болно.
	* [https://defuse.ca/online-x86-assembler.htm#disassembly2](https://defuse.ca/online-x86-assembler.htm#disassembly2) дараа нь **hex** хуулж авч доорх кодонд орлуулж бодож болно.
	
```C
char shellcode[] = "\xEF\xBE\xBE\xEA\x01\x9A\xAA\xBE\xEB\x0A\xAA\x01\x0B\xAB\xEE\xB0\xDA\xDD
\xAB\xEE\xB0\xCA\xDE\xB0\x12\xEE\xBE\xBE";

int main(int argc, char **argv){
  int (*fp) (int, int, int);
  fp = (void *)shellcode;
  int ret = fp(0xb5e8e971,0xc6b58a95,0xe20737e9);
  printf("ret = 0x%x\n", ret);
}	
// gcc asm3.c -o asm3_out -fno-stack-protector -z execstack -no-pie -m32
```

* `Test2`

