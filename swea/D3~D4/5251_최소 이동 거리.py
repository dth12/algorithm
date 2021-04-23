import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def solution():
    heap = []
    heappush(heap, (0, 0))

    while heap:
        w, v = heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w

            for i in range(N+1):
                if not visited[i]:
                    heappush(heap, (dist[v] + adj[v][i], i))

    return dist[N]


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())

    adj = [[1000000000 for _ in range(N+1)] for _ in range(N+1)]
    dist = [1000000000 for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(E):
        p, c, w = map(int, input().split())
        adj[p][c] = w

    print('#{} {}'.format(tc, solution()))
