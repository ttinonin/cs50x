#include "helpers.h"
#include <math.h>

int limit(int number);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int y =0; y<height;y++){
        for(int x = 0; x<width; x++){
            //pegas os valores rgb da imagem
            float blue = image[y][x].rgbtBlue;
            float red = image[y][x].rgbtRed;
            float green = image[y][x].rgbtGreen;

            int media = round((blue + red + green)/3);
            image[y][x].rgbtBlue = image[y][x].rgbtRed = image[y][x].rgbtGreen = media;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int y = 0; y<height;y++){
        for(int x = 0; x<width;x++){
            float red = image[y][x].rgbtRed;
            float green = image[y][x].rgbtGreen;
            float blue = image[y][x].rgbtBlue;

            float sephia_red = 0.393*red + 0.769*green + 0.189*blue;
            float sephia_green = 0.349*red + 0.686*green + 0.168*blue;
            float sephia_blue = 0.272*red + 0.534*green + 0.131*blue;

            int sepR = limit(round(sephia_red));
            int sepG = limit(round(sephia_green));
            int sepB = limit(round(sephia_blue));

            image[y][x].rgbtRed = sepR;
            image[y][x].rgbtBlue = sepB;
            image[y][x].rgbtGreen = sepG;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int y = 0; y<height;y++){
        for(int x =0;x<width/2;x++){
            RGBTRIPLE tmp = image[y][x];
            image[y][x]=image[y][width - (x+1)];
            image[y][width - (x+1)]=tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for(int y = 0; y<height;y++){
        for(int x = 0; x<width;x++){
            temp[y][x] = image[y][x];
        }
    }
    for(int y = 0; y<height;y++){
        for(int x=0;x<width;x++){
            float sr;
            float sb;
            float sg;
            int counter;
            sr = sb = sg = counter = 0;
            for(int i = -1; i < 2;i++){
                for(int j = -1; j < 2; j++){
                    if(((y+i)<0)||((y+i)>=height)){
                        continue;
                    }
                    if(((x+j)<0)||((x+j)>=width)){
                        continue;
                    }
                    sr += temp[y + i][x+j].rgbtRed;
                    sg += temp[y + i][x+j].rgbtGreen;
                    sb += temp[y + i][x+j].rgbtBlue;
                    counter++;
                }
            }
            image[y][x].rgbtRed = round(sr / counter);
            image[y][x].rgbtGreen = round(sg / counter);
            image[y][x].rgbtBlue = round(sb / counter);
        }
    }
    return;
}

int limit(int number){
    if(number>255){
        number = 255;
    }
    return number;
}