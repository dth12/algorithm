import sys
from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


def gravity(board: list) -> None:
    for c in range(N):
        stack = []
        for r in range(3 * N):
            L = len(stack)

            if board[r][c]:
                stack.append(board[r][c])
            else:
                for i in range(L):
                    board[r - i][c] = stack[L - i - 1]

                board[r - L][c] = 0


def bfs(row: int, col: int, idx: int, board: list) -> int:
    local_visited = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque([[row, col]])
    r_range = [row, row]
    c_range = [col, col]
    car_num = board[row + 2 * N][col]
    board[row + 2 * N][col] = 0
    cnt = 1
    local_visited[row][col] = 1
    if idx == 0: visited[row][col] = 1

    while Q:
        r, c = Q.popleft()

        r_range[0] = min(r_range[0], r)
        r_range[1] = max(r_range[1], r)
        c_range[0] = min(c_range[0], c)
        c_range[1] = max(c_range[1], c)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if inrange(nr, nc) and not local_visited[nr][nc] and board[nr + 2 * N][nc] == car_num:
                cnt += 1
                board[nr + 2 * N][nc] = 0
                local_visited[nr][nc] = 1
                Q.append([nr, nc])
                if idx == 0: visited[nr][nc] = 1

    square = (r_range[1] + 1 - r_range[0]) * (c_range[1] + 1 - c_range[0])
    return cnt + square


def solve(order: list) -> int:
    temp = 0
    copy = [[board[r][c] for c in range(N)] for r in range(3 * N)]

    for i in range(len(order)):
        r = order[i] // N
        c = order[i] % N
        temp += bfs(r, c, i, copy)
        gravity(copy)

    return temp


N = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
board = [list(map(int, input().split())) for _ in range(3 * N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
case = N * N

for i in range(case):
    if visited[i // N][i % N]: continue
    for j in range(case):
        for k in range(case):
            answer = max(solve([i, j, k]), answer)

print(answer)
