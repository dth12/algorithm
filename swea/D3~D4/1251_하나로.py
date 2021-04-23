import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop
# 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L2)만큼 지불
def dist(x1, y1, x2, y2: int) -> float:
    return ((x1 - x2)**2 + (y1- y2)**2)


def solution():

    total_cost = 0
    heap = []
    heappush(heap, (0, 0))
    while heap:
        cost, v = heappop(heap)
        if not visited[v]:
            visited[v] = 1
            total_cost += cost


            for i in range(N):
                if not visited[i]:
                    heappush(heap, (dist(x_pos[v], y_pos[v], x_pos[i], y_pos[i]), i))

    return total_cost

for tc in range(1, int(input())+1):
    N = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    visited = [0 for _ in range(N)]
    E = float(input())

    print('#{} {:.0f}'.format(tc, E*solution()))



