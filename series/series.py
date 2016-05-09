def slices(seq, width):

    if width not in range(1, len(seq)+1):
        raise ValueError("Invalid parameter values")

    return [map(int, list(seq[i:i + width]))
            for i in range(len(seq) - width + 1)]

