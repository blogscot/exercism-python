from string import lowercase, maketrans

alphabet = lowercase
tebahpla = alphabet[::-1]
CHUNK = 5


def chunk(sentence, size=CHUNK):
    """
    Breaks a string into chunks.

    :param sentence:        sentence to chunk
    :param size:            chunk size
    :return:                string of space separated chunks
    """

    if len(sentence) <= size:
        return sentence

    return ' '. join([''.join(list(item))
                      for item in zip(*[iter(sentence)]*size)])


def encode(seq):
    """
    Encodes a string into 5 character blocks

    :param seq:     sentence to encode
    :return:        Atbash encoded sentence
    """

    return chunk(seq
                 .lower()
                 .replace(" ", "")
                 .translate(maketrans(alphabet, tebahpla)))


def decode(seq):
    """
    Decodes an Atbash encoded string

    :param seq:     Atbash encoded sentence
    :return:        decoded sentence
    """

    return seq.translate(maketrans(tebahpla, alphabet))
