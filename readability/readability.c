#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>


int count_words(string texto);
int count_letters(string texto);
int sentence(string texto);

int main(void)
{
    int num, nota;
    string texto = get_string ("Text: ");
    int palavras = count_words(texto);
    num = count_letters(texto);
    int sentenca = sentence(texto);
    float grade = 0.0588 * (100 * num / palavras) - 0.296 * (100 * sentenca / palavras) - 15.8;
    float dif = grade - round(grade);
    if(grade>7.30 && grade<7.60){
        nota = floor(grade);
    }
    else{
        int first = round(grade);
        nota = (int)first;
    }

    if(nota>16){
        printf("Grade 16+\n");
    }
    if(nota<1){
        printf("Before Grade 1\n");
    }
    if (nota>1 && nota< 16){
        printf("Grade %d\n", nota);
    }
}

int count_words(string texto){
    int count= 1;
    for(int i=0; i<strlen(texto);i++){
        if(texto[i] == ' '){
            count++;
        }
    }
    return count;
}

int count_letters(string texto){
    int count=0;
    for(int i=0;i<strlen(texto);i++){
        if((texto[i] >= 'a' && texto[i]<='z')||(texto[i] >= 'A' && texto[i]<= 'Z')){
            count++;
        }
    }
    return count;
}

int sentence(string texto){
    int count = 0;
    for(int i = 0; i<strlen(texto); i++){
        if(texto[i] == '.'||texto[i]=='!'||texto[i]=='?'){
            count++;
        }
    }
    return count;
}