from math import log2

class Sparse:
    def __init__(self, a, func=min):
        self.a = a
        self.n = len(a)
        self.k = int(log2(self.n)) + 1
        self.func = func
        self.lookup = [[0] * self.k for _ in range(self.n)]
        self.process()

    def process(self):
        for i in range(self.n):
            self.lookup[i][0] = self.a[i]
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.lookup[i][j] = self.func(self.lookup[i][j - 1], 
                                              self.lookup[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, alpha, omega):
        """Query from alpha to omega (inclusive)!"""
        x = int(log2(omega - alpha + 1))
        return self.func(self.lookup[alpha][x], self.lookup[omega - (1 << x) + 1][x])
