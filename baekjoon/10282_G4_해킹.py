import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def solution(start):
    dist = [9876543210 for _ in range(N+1)]
    heap = []

    heappush(heap, (0, start))
    total = 0
    while heap:
        t, com = heappop(heap)

        if not visited[com]:
            visited[com] = 1
            dist[com] = t
            total += 1

            for i in adj[com]:
                if not visited[i]:
                    heappush(heap, (t + adj[com][i], i))

    MAX = 0
    for time in dist:
        if time != 9876543210:
            MAX = max(MAX, time)

    return total, MAX


for tc in range(1, int(input())+1):
    N, M, start = map(int, input().split())
    adj = [{} for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b, time = map(int, input().split())
        adj[b][a] = time

    print(*solution(start))