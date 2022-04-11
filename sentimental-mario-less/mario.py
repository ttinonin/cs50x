from cs50 import get_int


while(True):
    tamanho = get_int("Height: ")
    if(tamanho >= 9 or tamanho < 1 or tamanho == str or tamanho == []):
        continue
    else:
        break


espaco = tamanho - 1
for i in range(0, tamanho):
    print(((tamanho -1 -i) * ' '), end = '')
    print((i+1)*'#')