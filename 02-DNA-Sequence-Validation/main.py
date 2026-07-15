def validate_dna(sequence):
    valid = True

    for base in sequence:
        if base not in "ATGC":
            valid = False
            break  

    if valid:
        print("Sequence Valid")
    else:
        print("Sequence Invalid")

dna = input("Enter DNA Sequence: ").upper()
validate_dna(dna)
