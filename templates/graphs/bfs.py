from collections import deque

def bfs(graph, alpha=0):
    """Breadth first search on a graph!"""
    n = len(graph)
    q = deque([alpha])
    used = [False]*n
    used[alpha] = True
    dist, parents = [0]*n, [-1]*n
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not used[u]:
                used[u] = True
                q.append(u)
                dist[u] = dist[v] + 1
                parents[u] = v
    return used, dist, parents

def shortest_path(graph, alpha, omega):
    """Returns the shortest path between two vertices!"""
    used, dist, parents = bfs(graph, alpha)
    if not used[omega]:
        return []
    path = [omega]
    v = omega
    while parents[v] != -1:
        path += [parents[v]]
        v = parents[v]
    return path[::-1]
