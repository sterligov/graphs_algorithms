#Uses python3

import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    edges = []
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            edges.append({'from_v': i, 'to_v': adj[i][j], 'cost': cost[i][j]})
    distance[s] = 0
    reachable[s] = 1
    path = {}
    for _ in range(len(adj)-1):
        for e in edges:
            if distance[e['from_v']] != float("inf") and distance[e['to_v']] > distance[e['from_v']] + e['cost']:
                reachable[e['to_v']] = 1
                path[e['to_v']] = e['from_v']
                distance[e['to_v']] = distance[e['from_v']] + e['cost']
    q = []
    for e in edges:
        if distance[e['from_v']] != float("inf") and distance[e['to_v']] > distance[e['from_v']] + e['cost']:    
            q.append(e['to_v'])
    
    i = 0
    visited = [0] * len(adj)
    while len(q) > i:
        cur = q[i]
        i += 1
        if visited[cur] == 1:
            continue
        visited[cur] = 1
        shortest[cur] = 0
        for j in adj[cur]:
            q.append(j)
        # if shortest[e['to_v']] != 0 and distance[e['from_v']] != float("inf") and distance[e['to_v']] > distance[e['from_v']] + e['cost']:
        #     cur = e['from_v']
        #     while cur != e['to_v']:
        #         shortest[cur] = 0
        #         cur = path[cur]
        #     shortest[cur] = 0
    return


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
    s = data[0]
    s -= 1
    distance = [float("inf")] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

