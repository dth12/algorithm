def calc_answer(n: int):
    if n == 1:
        return 2
    else:
        x = calc_answer(n//2)
        if n % 2 == 0:
            return x * x % 1000000007
        else:
            return x * x * 2 % 1000000007


def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


def is_seperate(r: int, c: int) -> bool:
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not inrange(nr, nc):
            cnt += 1
        elif inrange(nr, nc) and board[nr][nc] == board[r][c]:
            cnt += 1

    if cnt == 4:
        return True

    return False


R, C = map(int, input().split())
board = [input() for _ in range(R)]
separated = 0
for r in range(R):
    for c in range(C):
        if is_seperate(r, c):
            separated += 1

print(calc_answer(separated))



