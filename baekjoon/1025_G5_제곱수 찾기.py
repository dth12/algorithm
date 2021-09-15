from math import sqrt


def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < M


def binary_search(n: int) -> int:
    start = 0
    end = int(sqrt(n)) + 1
    while start <= end:
        mid = (start + end) // 2

        mid_square = mid ** 2
        if mid_square < n:
            start = mid + 1
        elif mid_square == n:
            return n
        else:
            end = mid - 1

    return -1


def dfs(r: int, c: int, dr: int, dc: int, path: str) -> None:
    global answer

    answer = max(binary_search(int(path)), answer)
    nr = r + dr
    nc = c + dc
    if inrange(nr, nc):
        path += str(board[nr][nc])
        dfs(nr, nc, dr, dc, path)


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
answer = -1
for r in range(N):
    for c in range(M):
        for i in range(-N, N):
            for j in range(-M, M):
                if abs(i) + abs(j) >= 1:
                    dfs(r, c, i, j, str(board[r][c]))

print(answer)
