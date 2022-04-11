#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, linha;
    do{
        height = get_int("Height: ");
    }
    while(height> 8 || height < 1);

    for(linha = 0; linha < height; linha++){
        for(int espaco = 0; espaco < height - linha - 1; espaco++){
            printf(" ");
        }
        for(int coluna = 0; coluna <= linha; coluna++){
            printf("#");
        }
        for(int separa = 0; separa <2;separa++){
            printf(" ");
        }
        for(int i = 0; i<=linha; i++){
            printf("#");
        }
        printf("\n");
    }

}