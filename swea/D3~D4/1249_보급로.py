import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush
INF = 9876543210

def inrange(r, c):
    return 0 <= r < grid_size and 0 <= c < grid_size


def solution(start:list):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0]*grid_size for _ in range(grid_size)]
    dist = [[INF] * grid_size for _ in range(grid_size)]
    heap = []
    heappush(heap, (0, start[0], start[1]))
    while heap:
        cost, current_pos_r, current_pos_c = heappop(heap)

        if visited[current_pos_r][current_pos_c]: continue

        visited[current_pos_r][current_pos_c] = 1
        dist[current_pos_r][current_pos_c] = cost
        for i in range(4):
            moved_pos_r = current_pos_r + dr[i]
            moved_pos_c = current_pos_c + dc[i]

            if inrange(moved_pos_r, moved_pos_c):
                if not visited[moved_pos_r][moved_pos_c]:
                    current_cost = dist[current_pos_r][current_pos_c]
                    plus_cost = grid[moved_pos_r][moved_pos_c]
                    heappush(heap, (current_cost + plus_cost, moved_pos_r, moved_pos_c))

    return dist[grid_size-1][grid_size-1]



for tc in range(1, int(input())+1):
    grid_size = int(input())
    grid = [list((map(int, list(input())))) for _ in range(grid_size)]
    print('#{} {}'.format(tc, solution([0, 0])))

