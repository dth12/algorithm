import sys
sys.stdin = open('input.txt', 'r')


def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


def dust_spread(dust: list) -> None:
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    spreads = []
    for r, c in dust:
        cnt = 0
        amount = board[r][c] // 5
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc) and board[nr][nc] != -1:
                spreads.append([nr, nc, amount])
                cnt += 1

        board[r][c] -= cnt * amount

    for r, c, amount in spreads:
        board[r][c] += amount


def air_purify():
    r, c = purifier_pos[0]
    for i in range(4):
        while inrange(r + top_dr[i], c + top_dc[i]):
            nr = r + top_dr[i]
            nc = c + top_dc[i]

            if board[nr][nc] == -1:
                break

            if board[r][c] == -1:
                board[nr][nc] = 0
            else:
                board[r][c] = board[nr][nc]
                board[nr][nc] = 0

            r = nr
            c = nc

            if r == purifier_pos[0][0] and c == C - 1:
                break

    r, c = purifier_pos[1]
    for i in range(4):
        while inrange(r + bottom_dr[i], c + bottom_dc[i]):
            nr = r + bottom_dr[i]
            nc = c + bottom_dc[i]

            if board[nr][nc] == -1:
                break

            if board[r][c] == -1:
                board[nr][nc] = 0
            else:
                board[r][c] = board[nr][nc]
                board[nr][nc] = 0

            r = nr
            c = nc

            if r == purifier_pos[1][0] and c == C - 1:
                break


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

top_dr = [-1, 0, 1, 0]
top_dc = [0, 1, 0, -1]

bottom_dr = [1, 0, -1, 0]
bottom_dc = [0, 1, 0, -1]

purifier_pos = []

for r in range(R):
    if board[r][0] == -1:
        purifier_pos = [[r, 0], [r + 1, 0]]
        break

for _ in range(T):
    dust = []
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                dust.append([r, c])

    dust_spread(dust)
    air_purify()


cnt = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            cnt += board[r][c]

print(cnt)
