class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.func = lambda x, y: x if x[0] < y[0] else y
        self.default = (10**9, -1)
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        res = self.default
        alpha += self.size
        omega += self.size + 1
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

    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            index >>= 1

class LCA:
    def __init__(self, graph, root):
        self.graph = graph
        self.n = len(graph)
        self.euler = []
        self.first = [-1]*self.n
        self.st = None
        self.process(root)

    def process(self, root):
        visited, parents, heights = [False]*self.n, [-1]*self.n, [1]*self.n
        stack = [root]
        while stack:
            v = stack[-1]
            if not visited[v]:
                visited[v] = True
                self.euler += [v]
                if self.first[v] == -1:
                    self.first[v] = len(self.euler) - 1
                for u in self.graph[v]:
                    if not visited[u]:
                        stack.append(u)
                        parents[u], heights[u] = v, heights[v] + 1
            else:
                self.euler += [parents[stack.pop()]]
        self.euler = [(heights[k], k) for k in self.euler]
        self.st = SegmentTree(self.euler)

    def query(self, x, y):
        """Returns the lowest common ancestor of nodes x and y!"""
        p, q = min(self.first[x], self.first[y]), max(self.first[x], self.first[y])
        return self.st.query(p, q)[1]