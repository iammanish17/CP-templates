from math import log2, ceil


def kth_ancestor(x, k, ancestors):
    if k == 0: return x
    LOG = len(ancestors[0])
    for i in range(LOG - 1, -1, -1):
        if k & (1 << i):
            x = ancestors[x][i]
            k -= (1 << i)
            if x == -1: return x
    return x


def dfs(graph, alpha):
    """Depth First Search on a graph!"""
    n = len(graph)
    LOG = ceil(log2(n))
    visited = [False] * n
    stack = [alpha]
    ancestors = [[-1] * LOG for _ in range(n)]
    while stack:
        v = stack[-1]
        for i in range(1, LOG):
            ancestors[v][i] = ancestors[ancestors[v][i - 1]][i - 1]
        
        if not visited[v]:
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    ancestors[u][0] = v
                    stack.append(u)
        else:
            stack.pop()
    
    return ancestors