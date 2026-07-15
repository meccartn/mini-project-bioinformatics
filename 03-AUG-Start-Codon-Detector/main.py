def check_start_codon (sequence): 
  if sequence.startswith("AUG"):
    return "Valid Start Codon"
  else:
    return "Invalid Start Codon" 
sequence = input ("Enter RNA sequence: ").upper()
print(check_start_codon(sequence))
