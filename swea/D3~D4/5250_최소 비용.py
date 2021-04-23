import sys

sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop
def solution():
    heap = []
    heappush(heap, (dist[0][0], 0, 0))
    while heap:
        w, r, c = heappop(heap)

        if dist[r][c] > w:
            dist[r][c] = w
        else:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] - grid[r][c] > 0:
                    cost = grid[nr][nc] - grid[r][c]
                else:
                    cost = 0
                heappush(heap, (cost + 1 + w, nr, nc))


for tc in range(1, int(input())+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dist = [[100000000000 for _ in range(N)] for _ in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    solution()
    print('#{} {}'.format(tc, dist[N-1][N-1]))



# def solution():
#
#     min_idx = [0, 0]
#     for _ in range(N*N):
#         r, c = min_idx
#         for i in range(4):
#             nr = dr[i] + r
#             nc = dc[i] + c
#             if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#                 if grid[nr][nc] - grid[r][c] > 0:
#                     cost = grid[nr][nc] - grid[r][c]
#                 else:
#                     cost = 0
#                 copy[nr][nc] = min(copy[nr][nc], copy[r][c] + cost + 1)
#
#         visited[r][c] = 1
#
#         min_idx = [-1, -1]
#         min_val = 100000000
#         for x in range(N):
#             for y in range(N):
#                 if not visited[x][y] and copy[x][y] < min_val:
#                     min_idx = [x, y]
#                     min_val = copy[x][y]
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     copy = [[100000000 for _ in range(N)] for _ in range(N)]
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     copy[0][0] = 0
#     dr = [1, -1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     solution()
#     print('#{} {}'.format(tc, copy[N-1][N-1]))
