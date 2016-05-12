from string import lowercase, maketrans, punctuation

translations = maketrans(lowercase, lowercase[::-1])
CHUNK = 5


def filter_punctuation(sentence):
    return ''.join(filter(lambda s: s not in punctuation, sentence))


def chunk(sentence, size=CHUNK):
    return ' '.join([sentence[i:i+size] for i in range(0, len(sentence), size)])


def encode(seq):
    seq = seq.lower().replace(" ", "")
    seq = filter_punctuation(seq).translate(translations)
    return chunk(seq)


def decode(seq):
    return (seq
            .replace(" ", "")
            .translate(translations))

