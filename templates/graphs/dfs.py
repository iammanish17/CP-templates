def dfs(graph, alpha):
    """Depth First Search on a graph!"""
    n = len(graph)
    visited = [False]*n
    stack = [alpha]
    while stack:
        v = stack[-1]
        if not visited[v]:
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    stack.append(u)
        else:
            stack.pop()
    return visited