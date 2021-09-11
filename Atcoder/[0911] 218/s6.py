from heapq import heappush, heappop


INF = 16001
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
edges = []

heap = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    edges.append((a, b))

for i in range(M):
    heappush(heap, [0, 1])
    dist = [INF for _ in range(N + 1)]
    forbidden = edges[i]
    while heap:
        c, v = heappop(heap)

        if v == N:
            break

        if dist[v] < c: continue
        dist[v] = c

        for w in graph[v]:
            if (v, w) == forbidden: continue
            if c + 1 < dist[w]:
                dist[w] = c + 1
                heappush(heap, [c + 1, w])

    if dist[N] == INF:
        print(-1)
    else:
        print(dist[N])








