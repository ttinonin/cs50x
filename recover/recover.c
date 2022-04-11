#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //finds card.raw
    FILE *file = fopen(argv[1], "r");
    if(argc != 2){
        printf("Usage: ./recover file\n");
        return 1;
    }

    FILE *foto = NULL;
    int imgF = 0;
    unsigned char buffer[512];
    char *fileFound = malloc(8*sizeof(char));
    while(fread(buffer, sizeof(char), 512, file)){
        //confirm if the image is jpeg
        if(buffer[0]== 0xff && buffer[1] == 0xd8 && buffer[2]==0xff){
            //alocate the the file 0,1,2,3,4,5... in the array fileFound
            sprintf(fileFound, "%03i.jpg", imgF);
            foto = fopen(fileFound, "w");
            imgF++;
        }
        if (foto != NULL){
            fwrite(buffer, sizeof(char), 512, foto);
        }
    }
}