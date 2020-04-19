#Uses python3
import sys
import math
import heapq

def dfs(u, v, tree):
    stack = [u]
    visited = {}
    while len(stack) > 0:
        cur = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if cur in visited:
            continue
        visited[cur] = True
        for adj in tree[cur]:
            if adj == v:
                return True
            stack.append(adj)
    return False

def clustering(x, y, k):
    heap = []
    n = len(x)
    distance = [[] for i in range(n)]
    tree = [[] for i in range(n)]
    for i in range(n):
        distance[i] = [0 for i in range(n)]
        for j in range(i+1, n):
            distance[i][j] = euclideanDistance(x[i], y[i], x[j], y[j])
            heapq.heappush(heap, [distance[i][j], [i,j]])
    #search clusters
    visited = [0 for i in range(n)]
    minDistance = float("Infinity")
    spaningTreeHeap = []
    while len(heap) > 0:
        dist, edge = heapq.heappop(heap)
        if dfs(edge[0], edge[1], tree):
            continue
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
        heapq.heappush(spaningTreeHeap, [dist, edge])
    for i in range(k-1):
        dist, _ = spaningTreeHeap[len(spaningTreeHeap)-1]
        spaningTreeHeap = spaningTreeHeap[:len(spaningTreeHeap)-1]
        minDistance = min(minDistance, dist)
    if minDistance == float("Infinity"):
        return -1.
    return minDistance

def euclideanDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
