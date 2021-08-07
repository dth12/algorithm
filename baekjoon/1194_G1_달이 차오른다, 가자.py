from collections import deque


def possible_to_go(r: int, c: int, keys: list) -> bool:

    if not(0 <= r < R and 0 <= c < C):
        return False

    if 65 <= ord(board[r][c]) <= 90 and board[r][c] not in keys:
        return False

    case = 0
    for key in keys:
        case += 1 << (ord(key) - 64)

    if not visited[r][c][case] and board[r][c] != '#':
        return True

    return False


def visit(r: int, c: int, keys: list) -> None:
    case = 0
    for key in keys:
        case += 1 << (ord(key) - 64)

    visited[r][c][case] = 1


def bfs(start: list) -> int:
    Q = deque([[start[0], start[1], []]]) # 좌표와 갖고 있는 key를 체크.
    visit(start[0], start[1], [])

    dist = -1
    while Q:
        dist += 1
        L = len(Q)
        for _ in range(L):
            r, c, keys = Q.popleft()
            if r == 0 and c == 0:
                debug = True

            if board[r][c] == '1':
                return dist

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if possible_to_go(nr, nc, keys):
                    if 97 <= ord(board[nr][nc]) <= 122:
                        new_keys = keys[:]
                        if board[nr][nc].upper() not in new_keys:
                            new_keys += board[nr][nc].upper()
                        visit(nr, nc, new_keys)
                        Q.append([nr, nc, new_keys])
                    else:
                        visit(nr, nc, keys)
                        Q.append([nr, nc, keys])

    return -1


# 65 <= upper <= 90
# 97 <= lower <= 122
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[[0 for _ in range((2**7)-1)] for _ in range(C)] for _ in range(R)]
start = []

for r in range(R):
    for c in range(C):
        if board[r][c] == '0':
            start = [r, c]

print(bfs(start))
