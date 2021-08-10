import sys
sys.stdin = open('input.txt', 'r')

def inrange(r: int, c: int) -> bool:
   return 0 <= r < R and 0 <= c < C


def go_shark(direction: int, velocity: int, row: int, col: int, n: int) -> list:
    new_direction = direction
    r = row
    c = col
    for i in range(velocity):
        r += dr[new_direction]
        c += dc[new_direction]
        if not inrange(r, c):
            r -= dr[new_direction] * 2
            c -= dc[new_direction] * 2
            if new_direction in [1, 2]:
                new_direction = 1 if new_direction == 2 else 2
            elif new_direction in [3, 4]:
                new_direction = 3 if new_direction == 4 else 4

    sharks[n][3] = new_direction
    return [r, c, n]


def shark_move() -> list:
    new_board = [[-1 for _ in range(C)] for _ in range(R)]
    new_shark_pos = []
    for r in range(R):
        for c in range(C):
            if board[r][c] >= 0:
                n = board[r][c]
                direction = sharks[n][3]
                velocity = sharks[n][2]
                new_pos = go_shark(direction, velocity, r, c, n)
                new_shark_pos.append(new_pos)

    for i in range(len(new_shark_pos)):
        r, c, n = new_shark_pos[i]
        if new_board[r][c] == -1:
            new_board[r][c] = n
        else:
            m = new_board[r][c]
            if sharks[m][4] < sharks[n][4]:
                new_board[r][c] = n

    return new_board


def fishing(c: int) -> int:
    for r in range(R):
        if board[r][c] >= 0:
            shark_num = board[r][c]
            board[r][c] = -1
            return sharks[shark_num][4]

    return 0

# r c 속력 이동방향 크기
# 1 위, 2 아래, 3 오른쪽, 4 왼쪽
R, C, M = map(int, input().split())
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
board = [[-1 for _ in range(C)] for _ in range(R)]
sharks = [[] for _ in range(M)]
answer = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[i] = [r - 1, c - 1, s, d, z]
    board[r - 1][c - 1] = i


for c in range(C):
    answer += fishing(c)
    board = shark_move()

print(answer)

