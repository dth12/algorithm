INF = 20000 * 300000

def dijkstra(start: int):
    visited = [0] * (V + 1)
    dist[start] = 0
    for _ in range(V):
        min_cost = INF + 1
        min_idx = -1
        for i in range(1, V + 1):
            if not visited[i] and min_cost > dist[i]:
                min_cost = dist[i]
                min_idx = i

        v = min_idx
        visited[v] = 1

        for w in graph[v]:
            if not visited[w] and dist[w] > graph[v][w] + dist[v]:
                dist[w] = graph[v][w] + dist[v]


V, E = map(int, input().split())
start = int(input())

dist = [INF] * (V + 1)
graph = { i: dict() for i in range(1, V + 1) }

for i in range(E):
    s, e, cost = map(int, input().split())
    if e in graph[s]:
        if graph[s][e] > cost:
            graph[s][e] = cost
    else:
        graph[s][e] = cost

dijkstra(start)

for i in range(1, V + 1):
    if i == start:
        print(0)
    else:
        if dist[i] < INF:
            print(dist[i])
        else:
            print('INF')



