def translate (rna):
    prot = ""
    startIndex = 0
    while (rna[startIndex : startIndex+3] != "AUG"):
        startIndex += 1

    for i in range(startIndex ,len(rna)-3,3):
        codon = rna[i:i+3]
        if codon == "UUU" or codon == "UUC":
            prot= prot+ 'F'
        elif codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
            prot= prot+ 'L'
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG" or codon == "AGC" or codon == "AGU":
            prot= prot+ 'S'
        elif codon == "UAU" or codon == "UAC":
            prot= prot+ 'Y'
        elif codon == "UGU" or codon == "UGC":
            prot= prot+ 'C'
        elif codon == "UGG":
            prot= prot+ 'W'
        elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            prot= prot+ 'P'
        elif codon == "CAU" or codon == "CAC":
            prot= prot+ 'H'
        elif codon == "CAA" or codon == "CAG":
            prot= prot+ 'Q'
        elif codon == "CGU" or codon == "CGC":
            prot= prot+ 'R'
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            prot= prot+ 'I'
        elif codon == "AUG":
            prot= prot+ 'M'
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            prot= prot+ 'T'
        elif codon == "AAC" or codon == "AAU":
            prot= prot+ 'N'
        elif codon == "AAG" or codon == "AAA":
            prot= prot+ 'K'
        elif codon == "CGG" or codon == "AGG" or codon == "AGA" or codon == "CGA":
            prot= prot+ 'R'
        elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
            prot= prot+ 'V'
        elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            prot= prot+ 'A'
        elif codon == "GAC" or codon == "GAU" :
            prot= prot+ 'D'
        elif codon == "GAA" or codon == "GAG":
            prot= prot+ 'E'
        elif codon == "GGA" or codon == "GGC" or codon == "GGU" or codon == "GGG":
            prot= prot+ 'G'
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            break
    return prot, startIndex

if __name__ ==  "__main__":
    # with open("prot.txt") as file:
    #     rna = file.readline().strip()
    rna = "ACAUUUGCUUCUGACACAACUGUGUUCACUAGCAACCUCAAACAGACACCAUGGUGCACCUGACUCCUGAGGAGAAGUCUGCCGUUACUGCCCUGUGGGGCAAGGUGAACGUGGAUGAAGUUGGUGGUGAGGCCCUGGGCAGGCUGCUGGUGGUCUACCCUUGGACCCAGAGGUUCUUUGAGUCCUUUGGGGAUCUGUCCACUCCUGAUGCUGUUAUGGGCAACCCUAAGGUGAAGGCUCAUGGCAAGAAAGUGCUCGGUGCCUUUAGUGAUGGCCUGGCUCACCUGGACAACCUCAAGGGCACCUUUGCCACACUGAGUGAGCUGCACUGUGACAAGCUGCACGUGGAUCCUGAGAACUUCAGGCUCCUGGGCAACGUGCUGGUCUGUGUGCUGGCCCAUCACUUUGGCAAAGAAUUCACCCCACCAGUGCAGGCUGCCUAUCAGAAAGUGGUGGCUGGUGUGGCUAAUGCCCUGGCCCACAAGUAUCACUAAGCUCGCUUUCUUGCUGUCCAAUUUCUAUUAAAGGUUCCUUUGUUCCCUAAGUCCAACUACUAAACUGGGGGAUAUUAUGAAGGGCCUUGAGCAUCUGGAUUCUGCCUAAUAAAAAACAUUUAUUUUCAUUGC"
    print (translate(rna))
