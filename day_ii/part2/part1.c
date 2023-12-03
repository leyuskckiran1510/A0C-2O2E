#if 0
gcc -o $0.out $0 -lm && $0.out $@
rm $0.out &>/dev/null
exit
#endif
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(int argc,char **argv){
    if(argc<2){
        fprintf(stderr,"Please Provide a input file also\n");
        return -1;
    }
    char *filename = (++argv)[0];
    FILE *fp = fopen(filename,"r");
    
    return 0;
}

