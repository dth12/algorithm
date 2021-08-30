import sys
input = sys.stdin.readline


def find_root(start: int, end: int) -> list:
    path = [start]
    v = start
    w = end

    while v != w:
        v = next[v][w]
        path.append(v)

    return path


INF = 11109876543210

V = int(input())
E = int(input())

graph = [[0 if i == j else INF for i in range(V + 1)] for j in range(V + 1)]
next = [[None for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)
    next[start][end] = end

for mid in range(1, V + 1):
    for start in range(1, V + 1):
        for end in range(1, V + 1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]
                next[start][end] = next[start][mid]

for i in range(1, V + 1):
    for j in range(1, V + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

    print(*graph[i][1:])




