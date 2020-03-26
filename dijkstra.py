#Uses python3

import sys
from heapq import heappush, heappop

def distance(adj, cost, s, t):
    dis = [float("inf")] * len(adj)
    dis[s] = 0
    heap = []
    heappush(heap, (0, s))
    visited = {}
    while len(heap) > 0:
        cur = heappop(heap)
        if cur[1] in visited:
            continue
        if cur[1] == t:
            return dis[cur[1]]

        visited[cur[1]] = 1
        i = 0
        while i < len(adj[cur[1]]):
            if dis[cur[1]] + cost[cur[1]][i] < dis[adj[cur[1]][i]]:
                dis[adj[cur[1]][i]] = dis[cur[1]] + cost[cur[1]][i]
            heappush(heap, (dis[adj[cur[1]][i]], adj[cur[1]][i]))
            i += 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
