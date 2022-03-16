#include<stdio.h>

char s[9] = "You fail\x00";

struct vStruct {
	char buf1[8];
	char *buf;
}vulnBlock;

void fail(){
	puts("Fail\n");
}

int main(){
	puts("Welcome to new chall");
	vulnBlock.buf = (char *)malloc(4);
	
	int i;
	for(i=0;i<1;i++){
		gets(vulnBlock.buf1);
		printf("\n%s\n",vulnBlock.buf);
		gets(vulnBlock.buf);
		printf(vulnBlock.buf1);
	}
	fail();	
	exit(0);
}







