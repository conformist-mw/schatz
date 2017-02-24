#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <sys/io.h>

/* 31.12.2014 (mayton) - Happy new year, my dear geeks! HNE! */

void pc(int w,char c){
  while(w--) putchar(c);
}

void pcr(int w,char c,const char *r,float g){
  int l=strlen(r);
  while(w--) {
    float f=(((float)rand())*0xFFFF/RAND_MAX)/0xFFFF;
    if (f>g) putchar(c);
    else putchar(*(r + rand()%l));
  }
}


void pe(int w,int l1,int l2){
  int i;
  for(i=l1;i<l2;i++){
    int o=w-i;
    pc(o,' ');
    pcr(i,'/',"@&!+",0.1);
    pc(1,'|');
    pcr(i,'\\',"@&!+",0.1);
    putchar('\n');
  }
}

int main(int argc,char **arg, char **env){
  int i;
  for(i=0;i<20;i++){
    pe(40,i,3+i);
  };
  return 0;
}

