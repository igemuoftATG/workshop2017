def translateCodon (codon):
    if codon == "UUU" or codon == "UUC":
        return 'F'
    elif codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
        return 'L'
    elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG" or codon == "AGC" or codon == "AGU":
        return 'S'
    elif codon == "UAU" or codon == "UAC":
        return 'Y'
    elif codon == "UGU" or codon == "UGC":
        return 'C'
    elif codon == "UGG":
        return 'W'
    elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
        return 'P'
    elif codon == "CAU" or codon == "CAC":
        return 'H'
    elif codon == "CAA" or codon == "CAG":
        return 'Q'
    elif codon == "CGU" or codon == "CGC":
        return 'R'
    elif codon == "AUU" or codon == "AUC" or codon == "AUA":
        return 'I'
    elif codon == "AUG":
        return 'M'
    elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
        return 'T'
    elif codon == "AAC" or codon == "AAU":
        return 'N'
    elif codon == "AAG" or codon == "AAA":
        return 'K'
    elif codon == "CGG" or codon == "AGG" or codon == "AGA" or codon == "CGA":
        return 'R'
    elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
        return 'V'
    elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
        return 'A'
    elif codon == "GAC" or codon == "GAU" :
        return 'D'
    elif codon == "GAA" or codon == "GAG":
        return 'E'
    elif codon == "GGA" or codon == "GGC" or codon == "GGU" or codon == "GGG":
        return 'G'
    elif codon == "UAA" or codon == "UAG" or codon == "UGA":
        return "END"

if __name__ ==  "__main__":
    with open("prot.txt") as file:
        rna = file.readline().strip()
    print (translate(rna))
