import sys
from collections import deque
input = sys.stdin.readline
def bfs(start: list):
    global size
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    Q = deque([start]) # 첫 시작을 넣어줍니다.
    visited = [[0 for _ in range(N)] for _ in range(N)] # 방문처리
    visited[start[0]][start[1]] = 1
    time = 0 # 이동시간을 적습니다.
    flag = 0 # 먹이를 찾으면 올려줍니다.
    eat = [] # 현재 거리에서 찾은 모든 먹이를 고릅니다.
    while Q:
        if flag: break # 만약 먹이를 찾으면 끝냅니다.
        L = len(Q)
        eat = []
        time += 1
        for _ in range(L):
            r, c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc] and grid[nr][nc] <= size:
                        Q.append([nr, nc])
                        visited[nr][nc] = 1
                        if 0 < grid[nr][nc] < size: # 나보다 작으면 먹이로 추가합니다.
                            eat.append([nr, nc])
                            flag = 1


    # 먹이를 찾았으면,
    if flag:
        # 최대한 위로, 최대한 왼쪽으로
        eat.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return eat.pop(), time
    else: # 찾지 못했으면
        return 0, 0


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
size = 2
answer = 0
start = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == 9:
            start = [r, c]
            grid[r][c] = 0
            break

    if start: break

exp = 0
while True:

    T, time = bfs(start)
    if not T: break

    grid[T[0]][T[1]] = 0
    exp += 1
    answer += time
    start = T

    # 나의 사이즈와 경험치가 같으면, 사이즈를 하나 올려줍니다.
    if exp == size:
        size += 1
        exp = 0


print(answer)
