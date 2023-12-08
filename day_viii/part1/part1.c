#include <stdint.h>
#include <string.h>
#if 0
gcc -O3 -o $0.out -Wall -Wextra  -pedantic $0 -lm && $0.out $@ #-fsanitize=address 
rm $0.out &>/dev/null
exit
#endif
#include<stdio.h>
#include<stdlib.h>
#include<math.h>


#define READ_MAX 1000
#define HASH_MAX  0xffffff         //0x44ac
#define RUN_MAX 300

uint runs[RUN_MAX] = {0};
int runCount = 0;
int padding[1000];
uint32_t hastable[HASH_MAX][2]={0};
char readBuffer[READ_MAX] ={0};

void init_run(char *line){
    while (line[runCount]!='\0') {
        // If true then 1, else 0, as L is 0index and R is 1index in a pair of (X,Y)
        runs[runCount] = line[runCount]=='R';
        runCount++;
    }
}

uint32_t hash(char *key){
    uint32_t hs = 0;
    hs = (hs<<8)|key[0];//0<<8 does nothing and hs = key[0] [key[0]==ff,for example]
    hs = (hs<<8)|key[1];//shift's key[0] by 8bit to form 0xff00|key[1]==>0xffaa[key[1]==aa]
    hs = (hs<<8)|key[2];//similar to above, 0xffaa00|key[2]
    return hs%HASH_MAX;
}
int main(int argc,char **argv){
    if(argc<2){
        printf("Please Provide a input File\n");
        return  1;
    }
    memset((void *)hastable,0,HASH_MAX*sizeof(hastable[0]));
    char *filename = argv[1];
    FILE *fp = fopen(filename,"r");
    fscanf(fp,"%[LR]\n\n",readBuffer);
    init_run(readBuffer);
    char key[4],value1[4],value2[4];
    uint32_t first=0;
    while(!feof(fp)){
        fscanf(fp,"%[A-Z] = (%[A-Z], %[A-Z])\n",key,value1,value2);
        uint32_t index = hash(key);
        if(first==0){
            first = index;
        }
        if(hastable[index][0]!=0){
            printf("hash collided %s => %d\n",key,index);
            printf("hastable has %d %d",hastable[index][0],hastable[index][1]);
            fclose(fp);
            return 0;
        }
        if(index>HASH_MAX){
            printf("more than could handle %c%c%c\n",(index>>16&0xff),(index>>8&0xff),(index>>0&0xff));
            fclose(fp);
            return 0;
        }
        hastable[index][0] = hash(value1);
        hastable[index][1] = hash(value2);
        // printf("%x %s\n",index,key);
        // printf("%x %s\n",hash(value1),value1);
        // printf("%x %s\n",hash(value2),value2);
    }
    uint32_t dest = hash("ZZZ");
    uint32_t ans = first;
    int count=0;
    while(ans!=dest){
        // printf("%s = (%s, %s)\n",(char *)&ans,(char *)&hastable[ans][0],(char *)&hastable[ans][1]);
        ans=hastable[ans][runs[count%runCount]];
        // printf("%x %s [%d] {%d}(%c)\n",ans,(char *)&ans,count,runs[count%runCount],runs[count%runCount]?'R':'L');
        count++;
        printf("%d\n",count);
    }
    printf("Total Count %d\n",count);
    fclose(fp);

    return 0;
}

