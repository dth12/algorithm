import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop
INF = 9876543210
def solution(start: int) -> list:

    visited = [0] * (num_of_towns+1)
    heap = []
    dist = [INF] * (num_of_towns+1)
    heappush(heap, (0, start))

    while heap:

        time, current_pos = heappop(heap)

        if not visited[current_pos]:
            visited[current_pos] = 1
            dist[current_pos] = time

            # adj_node is a key of dict
            for adj_node in adj[current_pos]:
                if not visited[adj_node]:
                    time = adj[current_pos][adj_node] + dist[current_pos]
                    heappush(heap, (time, adj_node))


    for i in range(num_of_towns+1):
        if dist[i] == INF:
            dist[i] = 0

    return dist


for tc in range(1, int(input())+1):
    num_of_towns, num_of_rails, X = map(int, input().split())

    adj = [dict() for _ in range(num_of_towns+1)]

    for _ in range(num_of_rails):
        from_, to_, cost = map(int, input().split())
        adj[from_][to_] = cost


    X_to_towns = []
    towns_to_X = [0] * (num_of_towns+1)
    for start in range(1, num_of_towns+1):
        if start == X:
            X_to_towns = solution(start)
        else:
            towns_to_X[start] = solution(start)[X]

    MAX_dist = 0
    for i in range(1, num_of_towns+1):
        if MAX_dist < towns_to_X[i] + X_to_towns[i]:
            MAX_dist = towns_to_X[i] + X_to_towns[i]

    print('#{} {}'.format(tc, MAX_dist))














