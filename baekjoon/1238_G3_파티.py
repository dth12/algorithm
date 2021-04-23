import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

def solution(town, des):

    dist = [100000000000 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist[0] = 0

    heap = []
    heappush(heap, (0, town))
    while heap:
        w, v = heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w

            if town != des:
                if v == des:
                    return dist

            for i in adj[v]:
                if not visited[i]:
                    heappush(heap, (w + adj[v][i], i))

    return dist



N, M, X = map(int, input().split())
adj = [{} for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    adj[v1][v2] = w

X_to_town = solution(X, X)
town_to_X = [1000000000000] * (N+1)
for i in range(1, N+1):
    if i == X: continue
    town_to_X[i] = solution(i, X)[X]

answer = 0
for i in range(1, N+1):
    temp = town_to_X[i] + X_to_town[i]
    if temp < 1000000000000:
        answer = max(answer, temp)

print(answer)