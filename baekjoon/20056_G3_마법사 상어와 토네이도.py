import sys
input = sys.stdin.readline

def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


def tornado(r: int, c: int, o: int, cur_sand: int) -> int:
    move = [1, 2, 1]
    ratio = [[0.01], [0.07, 0.02], [0.1]]
    spread = 0
    disappear = 0
    o1 = (o + 3) % 4
    o2 = (o + 1) % 4

    for i in range(3):
        for j in range(1, move[i] + 1):
            nr = r + dr[o1] * j + dr[o] * i
            nc = c + dc[o1] * j + dc[o] * i
            mr = r + dr[o2] * j + dr[o] * i
            mc = c + dc[o2] * j + dc[o] * i

            temp_n = int(cur_sand * ratio[i][j - 1])
            temp_m = int(cur_sand * ratio[i][j - 1])

            spread += (temp_n + temp_m)

            if inrange(nr, nc):
                board[nr][nc] += temp_n
            else:
                disappear += temp_n

            if inrange(mr, mc):
                board[mr][mc] += temp_m
            else:
                disappear += temp_m

    nr = r + dr[o] * 3
    nc = c + dc[o] * 3
    temp = int(cur_sand * 0.05)
    spread += temp
    if inrange(nr, nc):
        board[nr][nc] += temp
    else:
        disappear += temp

    nr = r + dr[o] * 2
    nc = c + dc[o] * 2
    remain = cur_sand - spread
    if inrange(nr, nc):
        board[nr][nc] += remain
    else:
        disappear += remain

    return disappear


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

answer = 0
o = 0
dist = 2
cnt = 0
r, c = N // 2, N // 2
while True:

    if o == 4:
        o -= 4

    nr = r + dr[o]
    nc = c + dc[o]

    if nr < 0 or nc < 0:
        break

    cur_sand = board[nr][nc]
    if cur_sand:
        answer += tornado(r, c, o, cur_sand)
        board[nr][nc] = 0

    r, c = nr, nc
    cnt += 1

    if cnt == dist:
        dist += 2
        cnt = 0
        o += 1

    if cnt == dist // 2:
        o += 1

print(answer)