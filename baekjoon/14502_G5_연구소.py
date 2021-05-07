from itertools import combinations
from collections import deque

def inrange(r, c):
    return 0 <= r < R and 0 <= c < C


def bfs(stops:tuple, zeros:int) -> None:
    global max_value
    grid_copy = [[grid[r][c] for c in range(C)] for r in range(R)]
    for r, c in stops:
        grid_copy[r][c] = 1
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    Q = deque(virus)

    while Q:
        if zeros < max_value: return
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc) and grid_copy[nr][nc] == 0:
                Q.append([nr, nc])
                grid_copy[nr][nc] = 2
                zeros -= 1

    max_value = max(max_value, zeros)


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

max_value = 0
virus = []
zero_pos = []
zeros = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == 2:
            virus.append([r, c])
        elif grid[r][c] == 0:
            zero_pos.append([r, c])
            zeros += 1

combs = list(combinations(zero_pos, 3))
for comb in combs:
    bfs(comb, zeros)

print(max_value-3)

