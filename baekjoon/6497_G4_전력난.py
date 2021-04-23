import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def prim(start):
    visited = [0] * num_of_houses
    answer = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        cost, current_pos = heappop(heap)
        if visited[current_pos]: continue
        visited[current_pos] = 1
        answer += cost

        for next_pos in adj[current_pos]:
            if not visited[next_pos]:
                heappush(heap,(adj[current_pos][next_pos], next_pos))

    return answer


while True:
    num_of_houses, num_of_rails = map(int, input().split())
    if num_of_houses == 0 and num_of_rails == 0:
        break
    adj = [dict() for _ in range(num_of_houses)]

    total_cost = 0
    for _ in range(num_of_rails):
        start, end, cost = map(int, input().split())
        adj[start][end] = cost
        adj[end][start] = cost
        total_cost += cost

    print(total_cost - prim(0))