from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


def bfs(row: int, col: int) -> None:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    Q = deque([[row, col]])
    visited[row][col] = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc) and board[nr][nc] and not visited[nr][nc]:
                Q.append([nr, nc])
                visited[nr][nc] = 1


T = int(input())

for _ in range(T):
    C, R, K = map(int, input().split())

    if K == C * R:
        print(1)
    else:
        answer = 0
        board = [[0 for _ in range(C)] for _ in range(R)]
        visited = [[0 for _ in range(C)] for _ in range(R)]
        for _ in range(K):
            c, r = map(int, input().split())
            board[r][c] = 1

        for r in range(R):
            for c in range(C):
                if board[r][c] == 0 or visited[r][c]: continue
                bfs(r, c)
                answer += 1

        print(answer)
