from rna import *
from prot import *
from hamm import *
from Bio import Entrez
from Bio import SeqIO
import math

def classifyMutation (dna1, dna2):

    rna1, rna2 = transcribe(dna1), transcribe(dna2)

    prot1, start1 = translate(rna1)[0], translate(rna1)[1]
    prot2, start2 = translate(rna2)[0], translate(rna2)[1]

    dna1 = dna1[start1:]
    dna2 = dna2[start2:]

    # Checking for frameshift
    if len(dna1) > len(dna2):
        # Frameshift mutations: Deletion
        return "Frameshift Mutation: Deletion has been detected!"
    elif len(dna1) < len(dna2):
        # Frameshift mutations: Insertion
        return "Frameshift Mutation: Insertion has been detected!"
    elif len(prot1) > len(prot2):
        # Nonsense mutation: two ways to do it
        return "Nonsense Mutation detected!"

    mutationCount = countPointMutation(dna1, dna2)

    if mutationCount == 0:
        # No mutation
        return "No mutation!"

    firstMutation = findFirstDiff(dna1, dna2)

    firstMutationAA = int(math.floor(firstMutation/3))

    mutatedAAFrom = prot1[firstMutationAA]
    mutatedAATo = prot2[firstMutationAA]

    # Types of point mutation:
    if mutatedAAFrom == mutatedAATo:
        #silent mutation
        return "Silent Mutation detected!"
    elif mutatedAAFrom != mutatedAATo:
        # Missense mutation
        return "Missense Mutation detected!"


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
    print (classifyMutation(dna1, dna2))
