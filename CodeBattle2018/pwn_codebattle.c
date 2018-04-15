#include <stdio.h>
#include <stdlib.h>
#include <time.h>
char *init(){
	char fmt[128];
	memset( fmt, 0, sizeof(fmt) );
	printf("\nEnter your name: ");
	fflush(stdout);
	int i = read(0,fmt,128);
	fflush(stdin);
	if(fmt[i-1] == 0x0A){
		fmt[i-1] = 0x00;	
	}
	printf("\nLet's start!\n");
	printf(fmt);
	return fmt;	
}
void run(){
	srand(time(NULL));
	int r = rand();
	int x;
	printf("\nEnter your lucky number: ");
	fflush(stdout);
	scanf("%d", &x);
	fflush(stdin);
	if(x==r){
		char str[128];
		FILE * file;
		file = fopen( "secret.txt" , "r");
		if (file) {
		    while (fscanf(file, "%s", str)!=EOF)
		        printf("%s",str);
		    fclose(file);
		}
	}
	else{
		exit(0);
	}	
}
int main(){
	printf("Wellcome to my game");
	printf("\n1. Enter your name.\n2. Play game.\n3. Exit");	
	char *name = NULL;
	int c;
	do{
		printf("\nEnter your choice:");
		fflush(stdout);
		scanf("%d", &c);
		switch(c){
			case 1: name = init(); break;
			case 2: run();break;
			case 3: exit(0);break;
			default: break;
		}
	}while(1);
return 0;
}

