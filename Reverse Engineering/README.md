## Reverse engineering

- `Stripped binary`

  - Stripped буюу хэрэгцээгүй debugging symbol ийг хаясан гэсэн үг. Ингэснээр тухайн програмыг reverse болон disassembly хийхэд хүндрэлтэй болж байгаа юм.

  - Тухайн binary файлыг аль санг ашигласныг мэдэж IDA дээрээ нэмж өгнө. [source](https://github.com/maroueneboubakri/lscan/wiki/Reverse-Engineer-a-stripped-binary-with-lscan-and-IDApro)

```
git clone https://github.com/maroueneboubakri/lscan.git
pip install pyelftools pefile
python lscan.py -S amd64/sig -f stripped
cp amd64/sig/libcrypto-1.0.2h.sig ../ida66/sig
```

- `Assembly language`

  - Машины хэл дээрх код бөгөөд ойлгож уншиж болно. Зарим үед хэт ойлгомжгүй байвал онлайн түүл ашиглаад diassemble хийгээд ажилуулж болно.
  - [https://defuse.ca/online-x86-assembler.htm#disassembly2](https://defuse.ca/online-x86-assembler.htm#disassembly2) дараа нь **hex** хуулж авч доорх кодонд орлуулж бодож болно.

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

```C
#include<stdio.h>
#include<string.h>

int main()
{
  unsigned char code[] = "\x55\x48\x89\xe5\x48\x83\xec\x18\x48\xc7\x45\xf8\x4f\x00\x00\x00\x48\xb8\x15\x4f\xe7\x4b\x01\x00\x00\x00\x48\x89\x45\xf0\x48\xc7\x45\xe8\x04\x00\x00\x00\x48\xc7\x45\xe0\x03\x00\x00\x00\x48\xc7\x45\xd8\x13\x00\x00\x00\x48\xc7\x45\xd0\x15\x01\x00\x00\x48\xb8\x61\x5b\x64\x4b\xcf\x77\x00\x00\x48\x89\x45\xc8\x48\xc7\x45\xc0\x02\x00\x00\x00\x48\xc7\x45\xb8\x11\x00\x00\x00\x48\xc7\x45\xb0\xc1\x21\x00\x00\x48\xc7\x45\xa8\xe9\x65\x22\x18\x48\xc7\x45\xa0\x33\x08\x00\x00\x48\xc7\x45\x98\xab\x0a\x00\x00\x48\xc7\x45\x90\xad\xaa\x8d\x00\x48\x8b\x45\xf8\x48\x0f\xaf\x45\xf0\x48\x89\x45\x88\x48\x8b\x45\xe8\x48\x0f\xaf\x45\xe0\x48\x0f\xaf\x45\xd8\x48\x0f\xaf\x45\xd0\x48\x0f\xaf\x45\xc8\x48\x89\x45\x80\x48\x8b\x45\xc0\x48\x0f\xaf\x45\xb8\x48\x0f\xaf\x45\xb0\x48\x0f\xaf\x45\xa8\x48\x89\x85\x78\xff\xff\xff\x48\x8b\x45\xa0\x48\x0f\xaf\x45\x98\x48\x0f\xaf\x45\x90\x48\x89\x85\x70\xff\xff\xff\xb8\x00\x00\x00\x00\xc9";
  int (*ret)() = (int(*)())code;

  ret();
}
```

- `Bypassing ptrace`

  - `Ghidra` open with raw binary, change **JNS** compare to **JMP** for disabling TEST instuction.

- `angr`

  - Нөхцөл шалгах, хэтэрхий статик байдалтай бичигдсэн **ELF** файлууд дээр гайхалтай үр дүнтэй энгийн template.
  - [Angr_template.py](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Reverse%20Engineering/Code/angr_template.py)

- `Random`

  - Brute force seed in [c-language](https://github.com/ByamB4/CCC/blob/master/Reverse%20Engineering/src/random-bruteforce-seed.c) (file based)
