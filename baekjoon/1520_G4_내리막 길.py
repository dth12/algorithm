from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
memo = [[0 for _ in range(C)] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
memo[R - 1][C - 1] = 1
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

Q = deque([[R - 1, C - 1]])
while Q:
    r, c = Q.popleft()
    if visited[r][c]: continue
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if inrange(nr, nc) and board[nr][nc] > board[r][c]:
            memo[nr][nc] += 1
            Q.append([nr, nc])

for i in memo:
    print(i)


# for r in range(R):
#     for c in range(C):
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if inrange(nr, nc) and board[nr][nc] < board[r][c]:
#                 memo[nr][nc] = 1 + memo[r][c]
#


