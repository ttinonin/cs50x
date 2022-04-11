import sys
import csv

def repeats(str, dna):
    i = 0
    while str*(i+1) in dna:
        i+=1
    return i

def find_element(strs, dna_fp, coluna):
    for str in strs:
        if dna_fp[str] != int(coluna[str]):
            return False
    return True

def main():
    if len(sys.argv) != 3:
        sys.exit('Usage: python dna.py data.csv sequence.txt')

    data = open(sys.argv[1], "r")
    sequences = open(sys.argv[2], "r")

    db_reader = csv.DictReader(data)
    strs = db_reader.fieldnames[1:]

    dna = sequences.read()
    sequences.close()


    dna_fp = {}
    for str in strs:
        dna_fp[str] = repeats(str, dna)

    #procula pela coluna de dna se é relacionado com as sequencias
    for coluna in db_reader:
        if find_element(strs, dna_fp, coluna):
            print(f"{coluna['name']}")
            data.close()
            return

    print("No match")
    data.close()

main()
