from string import lowercase, maketrans, punctuation

alphabet = lowercase
tebahpla = lowercase[::-1]
CHUNK = 5


def filter_punctuation(sentence):
    return ''.join(filter(lambda s: s not in punctuation, sentence))


def chunk(sentence, size=CHUNK):
    if len(sentence) <= size:
        return sentence

    return sentence[:size] + " " + chunk(sentence[size:])


def encode(seq):
    seq = seq.lower().replace(" ", "")
    seq = filter_punctuation(seq).translate(maketrans(alphabet, tebahpla))
    return chunk(seq)


def decode(seq):
    return (seq
            .replace(" ", "")
            .translate(maketrans(tebahpla, alphabet)))

