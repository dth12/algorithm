import sys
sys.stdin = open("input.txt", "r")


def dfs(start: list, cnt: int):
    global MAX
    MAX = max(MAX, cnt)

    if MAX == 18:
        debug = True

    r, c = start
    visited[r][c], visited[r][c - 1], visited[r - 1][c], visited[r - 1][c - 1] = 2, 1, 1, 1
    for nr in range(r, R):
        s = 1
        if nr == r:
            s = c

        for nc in range(s, C):
            if visited[nr][nc] == 0 and visited[nr][nc - 1] == 0 and visited[nr - 1][nc] == 0 and visited[nr - 1][
                nc - 1] == 0:
                flag = False
                for i in range(cnt + 2, all + 1):
                    if (nr, nc) in BT[i]:
                        flag = True
                        break

                if flag: continue
                BT[cnt].add((nr, nc))
                dfs([nr, nc], cnt + 1)

    visited[r][c], visited[r][c - 1], visited[r - 1][c], visited[r - 1][c - 1] = 0, 0, 0, 0


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(R)]
    visited = [[wafer[r][c] for c in range(C)] for r in range(R)]
    MAX = 0
    all = R * C // 2
    BT = [set() for _ in range(all + 1)]
    for row in range(1, R):
        for col in range(1, C):
            if visited[row][col] == 0 and visited[row - 1][col] == 0 and visited[row][col - 1] == 0 and \
                    visited[row - 1][col - 1] == 0:
                dfs([row, col], 1)

    print('#%d %d' % (tc, MAX))