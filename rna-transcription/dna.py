from string import maketrans


def to_rna(genes):
    return genes.translate(maketrans("GCTA", "CGAU"))
