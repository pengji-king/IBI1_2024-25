def find_cut_sites(dna_sequence, enzyme_sequence):#Finds the starting positions where a restriction enzyme cuts the DNA.
    # Convert both sequences to uppercase 
    dna_sequence = dna_sequence.upper()
    enzyme_sequence = enzyme_sequence.upper()

    # Validate sequences: only A, C, G, T
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    if not set(dna_sequence).issubset(valid_nucleotides):
        return "Error: DNA sequence contains invalid nucleotides."
    if not set(enzyme_sequence).issubset(valid_nucleotides):
        return "Error: Enzyme recognition sequence contains invalid nucleotides."

    # Find all starting positions of the recognition sequence
    cut_positions = []
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i + len(enzyme_sequence)] == enzyme_sequence:
            cut_positions.append(i)

    return cut_positions

dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
enzyme = "CATG"

cut_sites = find_cut_sites(dna, enzyme)
print(f"Cut sites found at positions: {cut_sites}")
