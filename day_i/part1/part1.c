#if 0
gcc -o $0.out $0 -lm && $0.out $@
rm $0.out &>/dev/null
exit
#endif
#include <stdio.h>
#include <stdlib.h>

#define println(x, ...) printf(x "\n", ##__VA_ARGS__)

int main(int argc, char **argv) {
  if (argc < 2) {
    println("Please provide input File");
    return -1;
  }
  char *filename = (++argv)[0];
  FILE *fp = fopen(filename, "r");
  int answer = 0, temp[2] = {0}, f = -1;
  char c;
  while (c != EOF) {
    c = fgetc(fp);
    if (c >= '0' && c <= '9') {
      if (f < 1) {
        f++;
      }
      temp[f] = c - '0';
    } else if (c == 10 || c == EOF) {
      answer += temp[0] * 10 + temp[f];
      f = -1;
    }
  }
  println("The answer is [%d]", answer);
  return 0;
}
