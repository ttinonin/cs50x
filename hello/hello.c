#include <cs50.h>
#include <stdio.h>

int main(void)
{
  string string_name = get_string("Whats your name?");

  printf("Hello %s\n", string_name);
}