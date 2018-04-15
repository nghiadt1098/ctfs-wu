#include <stdio.h>

int main(){

    FILE * f= fopen("output","rb");
     char buffer[100000];
    while (!feof(f)){
        fread(buffer,1,8665,f);
    }
    int i=0;
    for (i=0;i<8665;++i){
        buffer[i]=0xff-buffer[i];
    }
    FILE * k= fopen("out.jpg","wb");
    fwrite(buffer,1,8665,k);
    fclose(k);
}
