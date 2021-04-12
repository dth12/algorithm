import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    R, C, K = map(int, input().split())
    grid = [[0 for _ in range(C+2*K)] for _ in range(R+2*K)]
    copy = [[0 for _ in range(C+2*K)] for _ in range(R+2*K)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque([])
    for r in range(K, K+R):
        temp = list(map(int ,input().split()))
        for i in range(len(temp)):
            if temp[i] != 0:
                grid[r][K+i] = temp[i]
                queue.append([r, K+i])


    time = 0
    while time <= K:

        born = set()
        L = len(queue)
        for _ in range(L):
            v = queue.popleft()
            r = v[0]
            c = v[1]
            if grid[r][c] * 2 < copy[r][c]:
                pass
            elif grid[r][c] < copy[r][c]:
                copy[r][c] += 1
                queue.append([r, c])
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if grid[nr][nc] == 0:
                        born.add((nr, nc))
                        queue.append([nr, nc])
                        grid[nr][nc] = grid[r][c]
                        copy[nr][nc] = 1
                    elif (nr, nc) in born:
                        grid[nr][nc] = max(grid[r][c], grid[nr][nc])
            elif grid[r][c] >= copy[r][c]:
                queue.append(v)
                copy[r][c] += 1


        time += 1

    answer = 0
    for r in range(R+2*K):
        for c in range(C+2*K):
            if grid[r][c] != 0 and grid[r][c]*2 >= copy[r][c] :
                answer += 1

    print('#{} {}'.format(tc, answer))










