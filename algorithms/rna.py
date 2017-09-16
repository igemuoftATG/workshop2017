from Bio import Entrez
from Bio import SeqIO

def transcribe (dna):
    rna = ""
    for nucleotide in dna:
        if (nucleotide == 'T'):
            rna = rna + 'U'
        else:
            rna = rna + nucleotide
    return (rna)



def getDNAfromFasta (fastafile):
    path = "./fasta/" + fastafile
    with open(path, 'r') as file:
        seq_record = SeqIO.read(file, "fasta")
    sequence_object = seq_record.seq
    dna = str(sequence_object)
    return dna

if __name__ == "__main__":
    dna1 = getDNAfromFasta("test1-1.fasta")
    dna2 = getDNAfromFasta("test1-2.fasta")
    print (transcribe(dna1))
    print (transcribe(dna2))



# if __name__ ==  "__main__":
#     with open("rna.txt") as file:
#         dna = file.readline().strip()
#     print (transcribe(dna))
