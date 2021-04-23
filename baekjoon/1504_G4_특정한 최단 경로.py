import sys
sys.stdin = open("input.txt", "r")

INF = 9876543210
from heapq import heappush, heappop

def solution(start):
    dist = [INF] * (V+1)
    visited = [0] * (V+1)
    heap = []
    heappush(heap, (0, start))

    while heap:
        cost, current_pos = heappop(heap)
        if visited[current_pos]: continue
        visited[current_pos] = 1
        dist[current_pos] = cost

        for next_pos in adj[current_pos]:
            if not visited[next_pos]:
                heappush(heap, (dist[current_pos] + adj[current_pos][next_pos], next_pos))

    return dist


V, E = map(int, input().split())

adj = [dict() for _ in range(V+1)]
for _ in range(E):
    from_, to_, cost = map(int, input().split())
    # 양방향
    adj[from_][to_] = cost
    adj[to_][from_] = cost

# 반드시 거쳐가야 하는 정점 두 개.
v1, v2 = map(int, input().split())

first_to_other = solution(1)
last_to_other = solution(V)
v1_to_v2 = solution(v1)[v2]
first_to_v1 = first_to_other[v1]
first_to_v2 = first_to_other[v2]
last_to_v1 = last_to_other[v1]
last_to_v2 = last_to_other[v2]

first_v1_v2_last = first_to_v1 + v1_to_v2 + last_to_v2
first_v2_v1_last = first_to_v2 + v1_to_v2 + last_to_v1
answer = min(first_v1_v2_last, first_v2_v1_last)
if answer >= INF:
    answer = -1
print(answer)





