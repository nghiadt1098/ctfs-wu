#include <stdio.h>
#include <stdlib.h>

void login(){
	int password1;
	int password2;

	printf("enter password1 : ");
	fflush(stdout);
	scanf("%d", password1);
	fflush(stdin);

	
	printf("enter password2 : ");
        scanf("%d", password2);

	printf("checking...\n");
	if(password1==338150 && password2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
		exit(0);
        }
}

void welcome(){
	char name[100];
	printf("enter you name : ");
	fflush(stdout);
	scanf("%100s", name);
	printf("Welcome %s!\n", name);
}

int main(){
	printf("Login System\n");
	fflush(stdout);
	welcome();
	login();

	
	printf("Logged\n");
	return 0;	
}

