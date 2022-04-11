#include <cs50.h>
#include <stdio.h>

int get_card(void);


int main(void)
{
    int number = gat_card();

}

int get_card(void){
    int Cnumb;
    Cnumb = get_int ("Card number: ");
    return Cnumb;
}