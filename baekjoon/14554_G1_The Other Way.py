from heapq import heappush, heappop
import sys
input = sys.stdin.readline # 30만개 => 인풋 => 시간초과


def dijk() -> int:
    dist = [INF for _ in range(N + 1)]
    path = [0 for _ in range(N + 1)]
    dist[S] = 0
    path[S] = 1
    heap = [[0, S]]
    while heap:
        min_val, v = heappop(heap)
        if min_val > dist[v]: continue

        for cost, w in graph[v]:
            new_cost = dist[v] + cost
            if new_cost < dist[w]:
                heappush(heap, [new_cost, w])
                dist[w] = new_cost
                path[w] = path[v]
            elif dist[w] == new_cost:
                path[w] = (path[w] + path[v]) % 1000000009 # 메모리 초과

    return path[E]


N, M, S, E = map(int, input().split())
INF = 1000000000 * 100000 + 1
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])

print(dijk() % 1000000009)
