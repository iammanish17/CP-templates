from math import inf
from heapq import heappop, heappush

def dijkstra(graph, alpha):
    n = len(graph)
    distance = [inf]*n
    distance[alpha] = 0
    parents = [-1]*n
    queue = []
    heappush(queue, (0, alpha))
    while queue:
        length, v = heappop(queue)
        for x, dist in graph[v]:
            if dist + length < distance[x]:
                distance[x] = dist + length
                parents[x] = v
                heappush(queue, (dist+length, x))
    return distance, parents