// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <stdio.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = (LENGTH+1)*'z';
int palavra_counter = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int indice = hash(word);

    node *cursor = table[indice];
    while(cursor!=NULL){
        if(strcasecmp(cursor->word, word) == 0){
            return true;
        }
        cursor = cursor->next;
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int soma = 0;
    for(int i = 0; i < strlen(word);i++){
        soma+=tolower(word[i]);
    }

    return soma % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL){
        return false;
    }

    char word[LENGTH+1];
    //enquanto houver palavras no arquivo o programa irá lelas e colocar no array palavra
    while(fscanf(dict,"%s", word)!=EOF){
        node *nn = malloc(sizeof(node));
        if(nn == NULL){
            unload();
            return false;
        }
        strcpy(nn->word, word);
        nn->next=NULL;


        int indice = hash(word);
        node *head = table[indice];
        if(table[indice] == NULL){
            table[indice] = nn;
        }
        else{
            nn->next = table[indice];
            table[indice] = nn;

        }
        palavra_counter++;

    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return palavra_counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++){
        node *head = table[i];
        node *cursor = head;
        node *tmp = head;

        while (cursor != NULL){
            cursor = cursor->next;
            free(tmp);
            tmp=cursor;
        }
    }
    return true;
}