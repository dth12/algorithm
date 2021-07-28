def make_dragon_curve(cnt: int, path: list, gen: int) -> None:
    if cnt == gen:
        return

    rotate = {
        (0, 1): [1, 0],
        (1, 0): [0, -1],
        (0, -1): [-1, 0],
        (-1, 0): [0, 1],
    }

    L = len(path)
    last = path[-1]
    for i in range(L - 1, 0, -1):
        # 가장 마지막 지점에서 방향을 구함
        cr = path[i - 1][0] - path[i][0]
        cc = path[i - 1][1] - path[i][1]

        # 90도 회전한 방향에 마지막 지점의 값을 더해줌.
        nr = rotate[(cr, cc)][0] + last[0]
        nc = rotate[(cr, cc)][1] + last[1]

        # 마지막 점을 다시 끝에 넣어주고, board에 마킹
        last = [nr, nc]
        board[nr][nc] = 1
        path.append([nr, nc])

    make_dragon_curve(cnt + 1, path, gen)


N = int(input())
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
board = [[0 for _ in range(101)] for _ in range(101)]
for i in range(N):
    # d(방향) => 0 1 2 3 => 오른쪽, 위쪽, 왼쪽, 아래쪽
    c, r, d, g = map(int, input().split())
    board[r][c] = 1
    nr = r + dr[d]
    nc = c + dc[d]
    board[nr][nc] = 1
    make_dragon_curve(0, [[r, c], [nr, nc]], g)

cnt = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r][c + 1] and board[r + 1][c] and board[r + 1][c + 1]:
            cnt += 1

print(cnt)
