#Uses python3
import sys
import math
from heapq import heappush, heappop

def dis(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def minimum_distance(x, y):
    result = 0.
    n = len(x)
    distance = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        j = i
        while j < n:
            d = dis(x[i],y[i],x[j],y[j])
            distance[i][j] = d
            distance[j][i] = d
            j += 1
    heap = []
    heappush(heap, [0, 0])
    visited = [0] * n
    while len(heap) > 0:
        cur = heappop(heap)
        if visited[cur[1]] == 1:
            continue
        visited[cur[1]] = 1
        result += cur[0]
        for i in range(1, len(distance[cur[1]])):
            heappush(heap, [distance[cur[1]][i], i])
        
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
