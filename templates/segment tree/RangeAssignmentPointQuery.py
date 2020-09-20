from math import log2


class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 2 ** (int(log2(self.n - 1)) + 1) if self.n != 1 else 1
        self.default = None
        self.data = [self.default] * (2 * self.size)
        self.lazy = [None] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size: self.size + self.n] = array

    def push(self, index):
        """Push information of root to it's children!"""
        if self.lazy[index] is None: return
        self.lazy[2 * index] = self.lazy[index]
        self.lazy[2 * index + 1] = self.lazy[index]
        self.data[2 * index] = self.lazy[index]
        self.data[2 * index + 1] = self.lazy[index]
        self.lazy[index] = None

    def query(self, index):
        """Returns the value at given index!"""
        index += self.size
        for i in reversed(range(1, index.bit_length())):
            self.push(index >> i)
        return self.data[index]

    def update(self, alpha, omega, value):
        """Assign all elements in range (inclusive) to particular value."""
        alpha += self.size
        omega += self.size + 1
        for i in reversed(range(1, alpha.bit_length())):
            self.push(alpha >> i)
        for i in reversed(range(1, omega.bit_length())):
            self.push(omega >> i)
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] = value
                self.lazy[alpha] = value
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] = value
                self.lazy[omega] = value
            alpha >>= 1
            omega >>= 1