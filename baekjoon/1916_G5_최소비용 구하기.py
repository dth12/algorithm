import sys
input = sys.stdin.readline


def dijkstra() -> int:
    dist = [INF for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist[start] = 0
    for _ in range(N):
        min_val = INF
        min_idx = -1
        for i in range(1, N + 1):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                min_idx = i

        if min_idx == -1: break
        v = min_idx
        visited[v] = 1

        for w in range(1, N + 1):
            if not visited[w] and graph[v][w] >= 0:
                dist[w] = min(graph[v][w] + dist[v], dist[w])

    return dist[end]


INF = 11109876543210 # 1000 => 최대 도시 수, 100000 => 최대 비용
N = int(input().strip())
M = int(input().strip())
graph = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    to_, from_, cost = map(int, input().strip().split())
    if graph[to_][from_] >= 0:
        graph[to_][from_] = min(cost, graph[to_][from_])
    else:
        graph[to_][from_] = cost

start, end = map(int, input().split())
print(dijkstra())

