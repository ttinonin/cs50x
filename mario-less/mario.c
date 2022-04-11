#include <stdio.h>
#include <cs50.h>

int main(void)
{
  int height;
  do{
      height = get_int ("Height: ");
  }
  while(height < 1 || height > 8);
  for(int linha = 0; linha < height; linha++){
      for(int espaco = 0; espaco < height - linha -1; espaco++){
          printf(" ");
      }
      for(int coluna = 0; coluna <= linha; coluna++){
          printf("#");
      }
      printf("\n");
  }
}