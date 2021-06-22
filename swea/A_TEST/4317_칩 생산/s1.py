import sys
sys.stdin = open("input.txt", "r")


def is_possible(r: int, c: int):
    if wafer[r][c] == 0 and wafer[r][c + 1] == 0 and wafer[r + 1][c] == 0 and wafer[r + 1][c + 1] == 0:
        return True
    return False


def dfs(r: int, c: int, cnt: int):
    global MAX

    MAX = max(MAX, cnt)

    if r == R - 1:
        bit_idx = 0
        for i in range(R):
            if wafer[i][c] == 2:
                bit_idx += 1 << i

        if memo[c][bit_idx] >= cnt:
            return
        else:
            memo[c][bit_idx] = cnt

        dfs(0, c + 1, cnt)
        return

    if c == C - 1:
        return

    if is_possible(r, c):
        wafer[r][c], wafer[r][c + 1], wafer[r + 1][c], wafer[r + 1][c + 1] = 2, 1, 1, 1
        dfs(r + 1, c, cnt + 1)
        wafer[r][c], wafer[r][c + 1], wafer[r + 1][c], wafer[r + 1][c + 1] = 0, 0, 0, 0

    dfs(r + 1, c, cnt)


T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    MAX = 0
    wafer = [list(map(int, input().split())) for _ in range(R)]
    memo = [[-1 for _ in range(2 ** R)] for _ in range(C)]
    dfs(0, 0, 0)
    print('#%d %d' % (tc, MAX))








