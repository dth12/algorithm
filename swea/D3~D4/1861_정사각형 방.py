
from collections import deque
def bfs(start: list) -> tuple:
    queue = deque([start])
    cnt = 0
    room = rooms[start[0]][start[1]]
    while queue:
        r, c = queue.popleft()
        num = rooms[r][c]
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < N and 0 <= nc < N:
                temp = rooms[nr][nc]
                if visited[nr][nc] == 0 and abs(num - temp) == 1:
                    room = min(room, temp)
                    queue.append([nr, nc])
                    visited[nr][nc] = cnt
                    cnt += 1

    return cnt, room


for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    answer = 100000000
    MAX = 0
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            cnt, room = bfs([r, c])
            if cnt > MAX:
                MAX = cnt
                answer = room

    print('#{} {} {}'.format(tc, answer, MAX-1))
