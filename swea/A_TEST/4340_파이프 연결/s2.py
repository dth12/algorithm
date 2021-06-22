def inrange(r: int, c: int):
    return 0 <= r < N and 0 <= c < N


def dfs(r: int, c: int, cnt: int, in_dir: int) -> None:
    global MIN

    if MIN < cnt + (N - r + 1) + (N - c + 1):
        return

    # if memo[r][c][in_dir] < cnt:
    #     return
    # else:
    #     memo[r][c][in_dir] = cnt

    if r == N - 1 and c == N - 1:
        if board[r][c] == 1 or board[r][c] == 6:
            MIN = cnt
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if inrange(nr, nc) and board[nr][nc] and not visited[nr][nc]:
            if 1 <= board[nr][nc] <= 2:
                for case in [1, 2]:
                    if case in connection[board[r][c]][i]:
                        board[nr][nc] = case
                        visited[nr][nc] = 1
                        dfs(nr, nc, cnt + 1, i)
                        visited[nr][nc] = 0
            elif 3 <= board[nr][nc] <= 6:
                for case in [3, 4, 5, 6]:
                    if case in connection[board[r][c]][i]:
                        board[nr][nc] = case
                        visited[nr][nc] = 1
                        dfs(nr, nc, cnt + 1, i)
                        visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    connection = {
        1: {
            0: [],
            1: [],
            2: [1, 3, 6],
            3: [1, 4, 5],
        },
        2: {
            0: [2, 3, 4],
            1: [2, 5, 6],
            2: [],
            3: [],
        },
        3: {
            0: [],
            1: [2, 5, 6],
            2: [],
            3: [1, 4, 5],
        },
        4: {
            0: [],
            1: [2, 5, 6],
            2: [1, 3, 5],
            3: [],
        },
        5: {
            0: [2, 3, 4],
            1: [],
            2: [1, 3, 6],
            3: [],
        },
        6: {
            0: [2, 3, 4],
            1: [],
            2: [],
            3: [1, 4, 5],
        },
    }
    N = int(input())
    memo = [[[5000, 5000, 5000, 5000] for _ in range(N)] for _ in range(N)]
    MIN = N * N
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    memo[0][0][3] = 1
    visited[0][0] = 1
    dfs(0, 0, 1, 3)
    print('#%d %d' % (tc, MIN))