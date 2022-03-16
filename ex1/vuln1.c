#include<stdio.h>

char s[9] = "You fail\x00";

struct vStruct {
	char buf1[8];
	char *buf;
}vulnBlock;

void win(){
	system("/bin/sh");
}

void fail(){
	printf("\n%s\n",s);
}

int main(){
	vulnBlock.buf = (char *)malloc(4);
	gets(vulnBlock.buf1);
	printf("\n%s\n",vulnBlock.buf1);	
	gets(vulnBlock.buf);
	fail();	
	return 0;
}







