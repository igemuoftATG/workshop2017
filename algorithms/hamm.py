from Bio import Entrez
from Bio import SeqIO

def countPointMutation (dna1, dna2):
    count = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
    return (count)

def findFirstDiff (dna1, dna2):
    for i in range(len(dna1)):
        if not dna1[i] == dna2[i]:
            return (i)
    return None
#
# if __name__ ==  "__main__":
#     with open("hamm.txt") as file:
#         dna1 = file.readline().strip()
#         dna2 = file.readline().strip()
#         print (countPointMutation(dna1, dna2))
#         print (findFirstDiff(dna1, dna2))


def getDNAfromFasta (fastafile):
    path = "./fasta/" + fastafile
    file = open(path, 'r')
    seq_record = SeqIO.read(file, "fasta")
    sequence_object = seq_record.seq
    dna = str(sequence_object)
    return dna

if __name__ == "__main__":
    dna1 = getDNAfromFasta("test1-1.fasta")
    dna2 = getDNAfromFasta("test1-2.fasta")
    print (countPointMutation(dna1, dna2))
    print (dna1[:findFirstDiff(dna1, dna2)])
