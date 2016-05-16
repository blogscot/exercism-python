

class Luhn:

    @staticmethod
    def _luhnify(num):
        seq = [1 if n % 2 == 0 else 2 for n in range(len(str(num)))][::-1]
        l0 = map(lambda x: int(x), list(str(num)))
        l1 = map(lambda x, y: x * y, l0, seq)
        return map(lambda x: x if x < 10 else x - 9, l1)

    def __init__(self, num):
        self.num = num
        self._addends = Luhn._luhnify(num)
        self._checksum = sum(self._addends)

    @staticmethod
    def create(num):
        tail = Luhn(num*10).checksum() % 10
        return num * 10 + (10 - tail if tail else 0)

    def addends(self):
        return self._addends

    def checksum(self):
        return self._checksum

    def is_valid(self):
        return self._checksum % 10 == 0

