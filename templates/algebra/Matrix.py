# Template for Matrix Operations
# Created by manish.17
# https://github.com/iammanish17/CP-templates
# ----- Usage -----
#m1 = Matrix(2, 2, [[2, 4],[3, 7]])
#m2 = Matrix(2, 2, [[3, 1],[5, 2]])
#print(m1 + m2)
#print(m1 - m2)
#print(m1*m2)
#print(m1**100)
# ------------------
class Matrix(object):
    def __init__(self, n, m, values, modulo=10**9+7):
        """Initialize a nxm matrix with given set of values!"""
        self.n = n
        self.m = m
        self.modulo = modulo
        if len(values) == n*m:
            self.values = values
        else:
            self.values = [i for k in values for i in k]

    def get_element(self, i, j):
        """Returns element A[i][j]"""
        return self.values[i*self.n + j]

    def __add__(self, other):
        """Add two matrices if they have the same order!"""
        if other.n != self.n or other.m != self.m:
            return None
        return Matrix(self.n, self.m,
                      [(self.values[i] + other.values[i])%self.modulo
                       for i in range(self.n*self.m)],
                      self.modulo)

    def __sub__(self, other):
        """Subtract two matrices if they have the same order!"""
        if other.n != self.n or other.m != self.m:
            return None
        return Matrix(self.n, self.m,
                      [(self.values[i] - other.values[i]) % self.modulo
                       for i in range(self.n*self.m)],
                      self.modulo)

    def __mul__(self, other):
        """Multiply two matrices if multiplication is possible!"""
        if self.m != other.n:
            return None
        result = [0]*(self.n * other.m)
        for i in range(self.n):
            for j in range(self.m):
                for k in range(other.m):
                    result[i*self.n + k] = \
                        (result[i*self.n + k] +
                         self.values[i*self.n + j] * other.values[j*other.n + k]) % self.modulo
        return Matrix(self.n, other.m, result, self.modulo)

    def __pow__(self, power):
        """Raises a matrix to some power!"""
        result = None
        cur = self
        b = bin(power)[2:]
        for i in range(len(b) - 1, -1, -1):
            if b[i] == '1':
                result = cur if result is None else result*cur
            cur *= cur
        return result

    def __repr__(self):
        return "Matrix({0})".format([[self.values[i*self.n+j] for j in range(self.m)]
                                     for i in range(self.n)])
