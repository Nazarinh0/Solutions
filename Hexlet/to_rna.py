def to_rna(dna):
    rna_dict = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna = ''
    for items in dna:
        rna += rna_dict[items]
    return rna


print(to_rna("ACGTGGTCTTAA"))
