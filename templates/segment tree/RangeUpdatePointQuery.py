from math import log2


class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.default = 0
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array

    def query(self, index):
        """Returns the value at given index!"""
        res = self.default
        index += self.size
        while index:
            res += self.data[index]
            index >>= 1
        return res

    def update(self, alpha, omega, value):
        """Increases all elements in the range (inclusive) by given value!"""
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] += value
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] += value
            alpha >>= 1
            omega >>= 1
