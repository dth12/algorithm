import sys

sys.setrecursionlimit(100000)
answer = 20000


def inrange(r: int, c: int, board: list) -> bool:
    return 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 0


def dfs(board: list, memo: list, r: int, c: int, o: int, time: int) -> None:
    global answer

    if time > answer:
        return

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    N = len(board)

    if (r == N - 1 and c == N - 1) or (r + dr[o] == N - 1 and c + dc[o] == N - 1):
        answer = min(memo[r][c][o], answer)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        mr = nr + dr[o]
        mc = nc + dc[o]
        ro = (o + 2) % 4
        if inrange(nr, nc, board) and inrange(mr, mc, board) and memo[nr][nc][o] > time and memo[mr][mc][ro] > time:
            memo[nr][nc][o] = time
            dfs(board, memo, nr, nc, o, time + 1)

    for i in [1, -1]:
        if o + i < 0:
            no = o + i + 4
        else:
            no = (o + i) % 4

        nr = r + dr[no]
        nc = c + dc[no]
        rno = (o + 2) % 4
        if inrange(nr, nc, board) and inrange(nr + dr[o], nc + dc[o], board) and memo[r][c][no] > time and memo[nr][nc][
            rno] > time:
            memo[r][c][no] = time
            dfs(board, memo, r, c, no, time + 1)

        mo = (o + 2) % 4  # 날개를 기준으로 돌리기
        if mo + i < 0:
            nmo = mo + i + 4
        else:
            nmo = (mo + i) % 4

        mr = r + dr[o]
        mc = c + dc[o]
        nmr = mr + dr[nmo]
        nmc = mc + dc[nmo]
        rnmo = (nmo + 2) % 4
        if memo[mr][mc][mo] < time: continue
        if inrange(nmr, nmc, board) and inrange(nmr + dr[mo], nmc + dc[mo], board) and memo[mr][mc][nmo] > time and \
                memo[nmr][nmc][rnmo] > time:
            memo[mr][mc][nmo] = time
            dfs(board, memo, mr, mc, nmo, time + 1)


def solution(board) -> int:
    global answer

    N = len(board)
    memo = [[[20001] * 4 for _ in range(N)] for _ in range(N)]
    memo[0][0][0] = 1
    dfs(board, memo, 0, 0, 0, 1)

    return answer