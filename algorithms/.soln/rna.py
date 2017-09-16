def transcribe (dna):
    rna = ""
    for nucleotide in dna:
        if (nucleotide == 'T'):
            rna = rna + 'U'
        else:
            rna = rna + nucleotide
    return (rna)

if __name__ ==  "__main__":
    with open("rna.txt") as file:
        dna = file.readline().strip()
    print (transcribe(dna))
