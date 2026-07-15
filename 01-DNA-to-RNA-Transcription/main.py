def dna_to_rna_transcription (dna):

  if all (base in "ATGC" for base in dna):
    rna= dna.replace("T", "U")
    return rna
  else:
    return "Invalid DNA sequence"
  
dna = input("Enter DNA sequence: ").upper()
rna = dna_to_rna_transcription(dna)
print("RNA sequence: ", rna)
