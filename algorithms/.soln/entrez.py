from Bio import Entrez
from Bio import SeqIO

Entrez.email = "abcdabcd@gmail.com"

with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="13788565") as handle:
    seq_record = SeqIO.read(handle, "fasta")

print(seq_record.seq[0:40])

records = list(SeqIO.parse("sample.fasta", "fasta"))
first_record = records[0]
first_sequence = str(first_record.seq)
print(first_sequence)
