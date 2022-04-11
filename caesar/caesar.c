#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Please enter a valid argument!\n");
        return 1;
    }
    for (int a = 0;a<strlen(argv[1]);a++){
        if(!isdigit(argv[1][a])){
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);
    string texto = get_string("plaintext: ");
    printf("ciphertext: ");
    for(int i=0; i<strlen(texto);i++){
        if(texto[i] >= 65 && texto[i] <= 90){
            int a = texto[i] -64;
            int b = ((key + a)%26)+64;
            printf("%c", b);
        }
        else if(texto[i] >= 97 && texto[i] <= 122){
            int a = texto[i] -96;
            int b = ((key + a)%26)+96;
            printf("%c", b);
        }
        else{
            printf("%c", texto[i]);
        }
    }
        printf("\n");
        return 0;
}