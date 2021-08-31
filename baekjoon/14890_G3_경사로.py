def inrange(row: int, col: int) -> bool:
    return 0 <= row < N and 0 <= col < N


def is_path(row: int, col: int, i: int) -> int:
    r = row
    c = col
    h = board[r][c]
    wall = [-1, -1]
    for _ in range(N - 1):
        if r == row + dr[i] * (N - 1) and c == col + dc[i] * (N - 1):
            return 1

        r += dr[i]
        c += dc[i]
        if not inrange(r, c): return 0
        if board[r][c] == h:
            continue

        elif board[r][c] == h + 1:
            cnt = 0
            nr = r
            nc = c
            while inrange(nr, nc) and cnt < L:
                nr -= dr[i]
                nc -= dc[i]
                if inrange(nr, nc) and board[nr][nc] == h and [nr, nc] != wall:
                    cnt += 1
                else:
                    return 0

            if cnt == L:
                h += 1
            else:
                return 0

        elif board[r][c] == h - 1:
            cnt = 1
            while inrange(r, c) and cnt < L:
                r += dr[i]
                c += dc[i]
                if inrange(r, c) and board[r][c] == h - 1:
                    cnt += 1
                else:
                    return 0

            if cnt == L:
                wall = [r, c]
                h -= 1
            else:
                return 0

        else:
            return 0

    return 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0]
dc = [0, 1]
answer = 0

for r in range(N):
    for c in range(N):
        if r == 0 or c == 0:
            for i in range(2):
                if not inrange(r + dr[i], c + dc[i]):
                    continue
                answer += is_path(r, c, i)

print(answer)