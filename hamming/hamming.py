def distance(seq1, seq2):
    return sum ([a != b for a, b in zip(seq1, seq2)])