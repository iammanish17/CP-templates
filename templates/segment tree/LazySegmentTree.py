from math import inf, log2


class LazySegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def push(self, index):
        """Push the information of the root to it's children!"""
        self.lazy[2*index] += self.lazy[index]
        self.lazy[2*index+1] += self.lazy[index]
        self.data[2 * index] += self.lazy[index]
        self.data[2 * index + 1] += self.lazy[index]
        self.lazy[index] = 0

    def build(self, index):
        """Build data with the new changes!"""
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1]) + self.lazy[index]
            index >>= 1

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        res = self.default
        alpha += self.size
        omega += self.size + 1
        for i in range(len(bin(alpha)[2:])-1, 0, -1):
            self.push(alpha >> i)
        for i in range(len(bin(omega-1)[2:])-1, 0, -1):
            self.push((omega-1) >> i)
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
            alpha >>= 1
            omega >>= 1
        return res

    def update(self, alpha, omega, value):
        """Increases all elements in the range (inclusive) by given value!"""
        alpha += self.size
        omega += self.size + 1
        l, r = alpha, omega
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] += value
                self.lazy[alpha] += value
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] += value
                self.lazy[omega] += value
            alpha >>= 1
            omega >>= 1
        self.build(l)
        self.build(r-1)