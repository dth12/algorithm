import sys
sys.stdin = open("input.txt", "r")

def inrange(row, col):
    return 0 <= row < N and 0 <= col < N


def dfs(r, c, dist):
    global MIN
    if dist > MIN:
        return
    elif r == N - 1 and c == N - 1:
        MIN = min(dist, MIN)
        return

    visited[r][c] = 1
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if inrange(nr, nc) and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, dist+board[nr][nc])
            visited[nr][nc] = 0

# greedy는 안 됩니다.
T = int(input())

for tc in range(1, T+1):
    # 2 * N - 1 만큼 이동.

    N = int(input())
    MIN = N * N * 10
    dr = [1, 0]
    dc = [0, 1]
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dfs(0, 0, board[0][0])
    print('#{} {}'.format(tc, MIN))
