#Uses python3

import sys

def negative_cycle(adj, cost):
    dis = [float("inf")] * len(adj)
    vertex = {}
    edges = []
    for i in range(len(adj)):
        vertex[i] = 1
        for j in range(len(adj[i])):
            edges.append({'from_v': i, 'to_v': adj[i][j], 'cost': cost[i][j]})
    while len(vertex) > 0:
        key = next(iter(vertex))
        dis[key] = 0
        del vertex[key]
        for _ in range(len(adj)-1):
            for e in edges:
                if dis[e['from_v']] != float("inf") and dis[e['to_v']] > dis[e['from_v']] + e['cost']:
                    if e['to_v'] in vertex:
                        del vertex[e['to_v']]
                    dis[e['to_v']] = dis[e['from_v']] + e['cost']
        for e in edges:
            if dis[e['from_v']] != float("inf") and dis[e['to_v']] > dis[e['from_v']] + e['cost']:
                return 1
    return 0


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
    print(negative_cycle(adj, cost))

