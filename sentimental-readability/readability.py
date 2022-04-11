from cs50 import get_string
from math import *

def count_letters(txt):
    letras = 0
    for i in range(len(txt)):
        if txt[i] == '.' or txt[i] == ' ' or txt[i]==',' or txt[i]=="'" or txt[i] == ':' or txt[i]=='?' or txt[i]=='!':
            continue
        else:
            letras+=1
    return letras

def count_words(txt):
    words = 1
    for i in range(len(txt)):
        if txt[i] == ' ':
            words+=1
        else:
            continue
    return words

def sentences_count(txt):
    sentences = 0
    for i in range(len(txt)):
        if txt[i] == '.' or txt[i] == '!' or txt[i] == '?':
            sentences+=1
        else:
            continue
    return sentences

def main():
    texto = get_string('Texto: ')

    letters = count_letters(texto)
    words = count_words(texto)
    sentences = sentences_count(texto)

    L = float((letters/words)*100)
    S = float((sentences/words)*100)
    grade = (0.0588 * L - 0.296 * S - 15.8)
    grade = round(grade)
    if(grade>16):
        print("Grade 16+\n")

    if(grade<1):
        print("Before Grade 1\n")

    if (grade>1 and grade< 16):
        print(f"Grade {grade}")


main()