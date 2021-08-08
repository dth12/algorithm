from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


def bfs():
    visited = [[[0, 0] for _ in range(C)] for _ in range(R)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    dist = -1
    Q = deque([[0, 0, 0]]) # r, c, sword
    while Q:
        dist += 1
        if dist > limit: return 'Fail'

        L = len(Q)
        for _ in range(L):
            r, c, sword = Q.popleft()
            if r == R - 1 and c == C - 1: return dist
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not inrange(nr, nc): continue
                if visited[nr][nc][sword]: continue
                if sword:
                    Q.append([nr, nc, sword])
                    visited[nr][nc][sword] = 1
                else:
                    if board[nr][nc] == 0:
                        Q.append([nr, nc, sword])
                        visited[nr][nc][sword] = 1
                    elif board[nr][nc] == 2:
                        Q.append([nr, nc, 1])
                        visited[nr][nc][1] = 1

    return 'Fail'


R, C, limit = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
print(bfs())