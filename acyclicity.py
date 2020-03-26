#Uses python3

import sys


def acyclic(adj):
    visited = {}
    i = 0
    while i < len(adj):
        if not dfs(adj, visited, i):
            return 1
        i += 1
    return 0

def dfs(adj, visited, node):
    visited[node] = True
    i = 0
    while i < len(adj[node]):
        if adj[node][i] in visited:
            return False
        if not dfs(adj, visited, adj[node][i]):
            return False
        i += 1
    del visited[node]
    return True

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
