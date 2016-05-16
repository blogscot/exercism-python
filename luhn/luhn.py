

class Luhn:

    @staticmethod
    def create1(num):
        seq = [2 if n % 2 == 0 else 1 for n in range(len(str(num)))][::-1]
        l0 = map(lambda x: int(x), list(str(num)))
        l1 = map(lambda x, y: x * y, l0, seq)
        return map(lambda x: x if x < 10 else x - 9, l1)

    def luhnify(self, num):
        seq = [1 if n % 2 == 0 else 2 for n in range(len(str(num)))][::-1]
        l0 = map(lambda x: int(x), list(str(num)))
        l1 = map(lambda x, y: x * y, l0, seq)
        return map(lambda x: x if x < 10 else x - 9, l1)

    def __init__(self, num):
        self.num = num
        self._addends = self.luhnify(num)
        self._checksum = sum(self._addends)

    @staticmethod
    def create(num):
        t = (10 - sum(Luhn.create1(num)) % 10) % 10
        return int(str(num) + str(t))

    def addends(self):
        return self._addends

    def checksum(self):
        return self._checksum

    def is_valid(self):
        return self._checksum % 10 == 0

