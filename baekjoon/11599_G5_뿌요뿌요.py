from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < 12 and 0 <= c < 6


def bfs(row: int, col: int) -> bool:
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    Q = deque([[row, col]])
    path = []
    color = board[row][col]
    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[row][col] = 1

    while Q:
        r, c = Q.popleft()
        path.append([r, c])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc) and not visited[nr][nc] and board[nr][nc] == color:
                Q.append([nr, nc])
                visited[nr][nc] = 1

    if len(path) >= 4:
        for r, c in path:
            board[r][c] = '.'
        return True
    else:
        return False


def gravity() -> None:
    for c in range(6):
        stack = []
        for r in range(12):
            if board[r][c] == '.':
                L = len(stack)
                for i in range(L):
                    board[r - i][c] = stack[L - i - 1]
                    board[r - i - 1][c] = '.'
            else:
                stack.append(board[r][c])


board = [list(input()) for _ in range(12)]
answer = 0

flag = 1
while flag:
    flag = 0
    for r in range(12):
        for c in range(6):
            if board[r][c] == '.': continue
            if bfs(r, c): flag = 1

    gravity()

    if flag:
        answer += 1

print(answer)
