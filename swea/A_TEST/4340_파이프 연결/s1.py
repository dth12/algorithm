import sys
sys.stdin = open("input.txt", "r")


def inrange(r: int, c: int):
    return 0 <= r < N and 0 <= c < N

def dfs(r: int, c: int, in_dir: int):
    if 1 <= board[r][c] <= 2:
        if 0 <= in_dir <= 1:
    else:


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MIN = 2500
    memo = [[[5000, 5000, 5000, 5000] for _ in range(N)] for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    memo[0][0][3] = 1
    visited[0][0] = 1
    dfs(0, 0, 1, 3)
    print('#%d %d' % (tc, MIN))