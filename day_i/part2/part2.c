#if 0
gcc -o $0.out $0 -lm && $0.out $@
rm $0.out &>/dev/null
exit
#endif

#include <stdio.h>
#include <string.h>

#define println(x, ...) printf(x "\n", ##__VA_ARGS__)

#define MAX_WIDTH 100

static char VALIDS[10][6] = {
    "zero", "one", "two",   "three", "four",
    "five", "six", "seven", "eight", "nine",
};

int fchars[26] = {
    0 /*a*/, 0 /*b*/, 0 /*c*/, 0 /*d*/, 5 /*e*/,     4 /*f*/,     0 /*g*/,
    0 /*h*/, 0 /*i*/, 0 /*j*/, 0 /*k*/, 0 /*l*/,     0 /*m*/,     4 /*n*/,
    3 /*o*/, 0 /*p*/, 0 /*q*/, 0 /*r*/, 3 /*3|5 s*/, 3 /*3|5 t*/, 0 /*u*/,
    0 /*v*/, 0 /*w*/, 0 /*x*/, 0 /*y*/, 4 /*z*/,
};

int parse_line(char *line) {
  int first = -1, last = -1;
  int ptr1 = 0, ptr2 = 0;
  int length = strlen(line);
  while (line[ptr1]) {
    int fIndex = fchars[line[ptr1] - 'a'];
    if (line[ptr1] >= '0' && line[ptr1] <= '9') {
      if (first < 0) {
        first = line[ptr1] - '0';
      } else {
        last = line[ptr1] - '0';
      }
    } else if (fIndex && fIndex + ptr1 < length) {
      char newStr1[fIndex];
      char newStr2[5];
      memcpy(newStr1, &line[ptr1], fIndex);
      memcpy(newStr2, &line[ptr1], 5);
      for (int j = 0; j < 10; j++) {
        if (strcmp(newStr1, VALIDS[j]) == 0 ||
            strcmp(newStr2, VALIDS[j]) == 0) {
          if (first < 0) {
            first = j;
          } else {
            last = j;
          }
        }
      }
      memset(newStr1, '\0', fIndex);
      memset(newStr2, '\0', fIndex);
    }
    ptr1++;
  }
  return first * 10 + (last < 0 ? first : last);
}

int main(int argc, char **argv) {
  if (argc < 2) {
    println("Please provide input File");
    return -1;
  }
  char *filename = (++argv)[0];
  FILE *fp = fopen(filename, "r");
  int answer = 0;
  char line[MAX_WIDTH] = {0};
  char *_;
  while (!feof(fp)) {
    _ = fgets(line, MAX_WIDTH, fp);
    answer += parse_line(line);
  }

  println("The answer is [%d]", answer);
  return 0;
}
