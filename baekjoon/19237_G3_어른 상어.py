import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


def solve() -> int:
    queue = deque(initial_queue)
    visited = [1 for _ in range(M + 1)]
    time = 0
    while queue:
        if sum(visited) == 2:
            return time

        time += 1

        if time > 1000:
            return -1

        move = {}
        if time == 2:
            debug = True

        L = len(queue)
        for _ in range(L):
            r, c, direc, num = queue.popleft()
            if board[r][c]:
                order = prior[num][direc]
                flag = 1
                for i in order:
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if inrange(nr, nc) and smell[nr][nc][1] == 0:
                        flag = 0
                        smell[r][c][0] = num
                        smell[r][c][1] = K
                        board[r][c] = 0
                        if (nr, nc) in move:
                            move[(nr, nc)].append([num, i])
                        else:
                            move[(nr, nc)] = [[num, i]]
                        break

                if flag:
                    for i in order:
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if inrange(nr, nc) and smell[nr][nc][0] == num:
                            smell[r][c][0] = num
                            smell[r][c][1] = K
                            board[r][c] = 0
                            if (nr, nc) in move:
                                move[(nr, nc)].append([num, i])
                            else:
                                move[(nr, nc)] = [[num, i]]
                            break

        for pos in move:
            if len(move[pos]) > 1:
                move[pos].sort()
                for i in range(1, len(move[pos])):
                    visited[move[pos][i][0]] = 0

            r, c = pos
            num, direc = move[pos][0]
            board[r][c] = num
            queue.append([r, c, direc, num])

        for r in range(N):
            for c in range(N):
                if smell[r][c][1]:
                    smell[r][c][1] -= 1
                    if smell[r][c][1] == 0:
                        smell[r][c][0] = 0

    return time

# N => map size, M => 상어 번호, K => 냄새 지속시간
'''
    1. 1초마다 상하좌우로 이동
    2. 아무 냄새가 없는 칸으로 먼저 이동
    3. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.

'''
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
init_dir = list(map(int, input().split()))
prior = {key: {} for key in range(1, M + 1)}
for num in range(1, M + 1):
    for direction in range(1, 5):
        prior[num][direction] = list(map(int, input().split()))

initial_queue = []
for r in range(N):
    for c in range(N):
        if board[r][c]:
            initial_queue.append([r, c, init_dir[board[r][c] - 1], board[r][c]])

dr = {
    1: -1,  # 위
    2: 1,   # 아래
    3: 0,   # 왼쪽
    4: 0,   # 오른쪽
}
dc = {
    1: 0,
    2: 0,
    3: -1,
    4: 1,
}

print(solve())