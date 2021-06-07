class LinearRecurrence:
	def __init__(self, coefficients, values, mod = 10**9 + 7):
		self.coefficients = coefficients
		self.values = values
		self.mod = mod
		self.k = len(values)
		self.a = []
		self.b = []
		self.process()

	def process(self):
		self.a = [self.values]
		self.b = [[0] * self.k for _ in range(self.k)]
		i = 1
		while i < self.k:
			self.b[i][i-1] = 1
			i += 1
		for j in range(self.k):
			self.b[j][self.k - 1] = self.coefficients[-j-1]

	def multiply(self, A, B):
		return [[sum(i * j for i, j in zip(row, col)) % self.mod for col in zip(*B)] for row in A]

	def get_power(self, p):
		res = [[0] * self.k for _ in range(self.k)]
		cur = [list(x) for x in self.b]
		for i in range(self.k):
			res[i][i] = 1
		i = 0
		while p:
			if p & (1 << i):
				res = list(self.multiply(res, cur))
				p ^= (1 << i)
			cur = list(self.multiply(cur, cur))
			i += 1
		return res

	def get_term(self, n):
		if n <= self.k:
			return self.values[n - 1] % self.mod
		return self.multiply(self.a, self.get_power(n - self.k))[0][-1]