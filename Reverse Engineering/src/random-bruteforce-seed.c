#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
  FILE *flag;
  flag = fopen("./flag.txt", "rb");

  if (!flag) 
    printf("File not found");
  
  char ctext[6] = "";
  char etext[] = "flag{";
  char atext[6] = "";

  fread(&ctext, 1, 5, flag);

  for (int i = 0; i <= 0xFFFF; i++) {

    srand(i);
    // printf("%d\n", i);
    for (int c = 0; c < 5; c++)
      atext[c] = ctext[c] ^ rand();

    if (strncmp(atext, etext, strlen(etext)) == 0) {
      char f;
      printf("flag{");
      while (fread(&f, 1, 1, flag))
        printf("%c", f ^ rand());
      printf("\n");
      break;
    }
  }

  printf("[-] No solution found\n");
}
