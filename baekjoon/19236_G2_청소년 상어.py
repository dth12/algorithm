import sys
sys.stdin = open('input.txt', 'r')


'''
    1. 물고기는 번호 순서대로 이동. 현재 방향부터 45도 반시계 방향 회전.
    2. 이동할 공간 없으면 가지 않음.
    3. 이동하는 방법은 스왑
    4. 다 이동하면 상어 이동.
    5. 이동 중에는 잡어먹지 않고 도착 후, 잡아먹기
    6. 이동할 수 있는 공간이 없다면 집으로 감.
    
'''


def inrange(r: int, c: int) -> bool:
    return 0 <= r < 4 and 0 <= c < 4


def fish_move():
    global board, fishes
    for num in range(1, 17):
        alive, r, c, d = fishes[num]
        if not alive: continue
        for i in range(8):
            nd = d + i
            if nd >= 8: nd -= 8
            nr = r + dr[nd]
            nc = c + dc[nd]
            if inrange(nr, nc) and board[nr][nc] != 17:
                if board[nr][nc] == 0:
                    fishes[num][1], fishes[num][2], fishes[num][3] = nr, nc, nd
                    board[r][c] = 0
                    board[nr][nc] = num
                else:
                    swap_num = board[nr][nc]
                    board[r][c] = swap_num
                    board[nr][nc] = num
                    fishes[swap_num][1], fishes[swap_num][2] = r, c
                    fishes[num][1], fishes[num][2], fishes[num][3] = nr, nc, nd
                break


def dfs(shark_r: int, shark_c: int, shark_d, total: int, cnt: int):
    global answer, fishes, board

    answer = max(total, answer)
    if answer >= 30:
        debug = True

    if cnt == 16:
        return

    board_temp = [[board[i][j] for j in range(4)] for i in range(4)]
    fishes_temp = [[fishes[i][0], fishes[i][1], fishes[i][2], fishes[i][3]] for i in range(17)]

    for i in range(3, 0, -1):
        nr = shark_r + dr[shark_d] * i
        nc = shark_c + dc[shark_d] * i
        fish_move()
        if inrange(nr, nc) and 0 < board[nr][nc] < 17:
            num = board[nr][nc]
            fish_d = fishes[num][3]
            board[nr][nc] = 17
            fishes[num][0] = 0
            board[shark_r][shark_c] = 0
            dfs(nr, nc, fish_d, total + num, cnt + 1)

        board = [[board_temp[i][j] for j in range(4)] for i in range(4)]
        fishes = [[fishes_temp[i][0], fishes_temp[i][1], fishes_temp[i][2], fishes_temp[i][3]] for i in range(17)]


answer = 0
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

fishes = [[0, -1, -1, -1] for _ in range(17)] # alive, r, c, dir
board = [[0 for _ in range(4)] for _ in range(4)]

for r in range(4):
    temp = list(map(int, input().split()))
    for c in range(4):
        num = temp[c * 2]
        direction = temp[1 + (c * 2)] - 1
        fishes[num][0] = 1
        fishes[num][1] = r
        fishes[num][2] = c
        fishes[num][3] = direction
        board[r][c] = num

start = board[0][0]
board[0][0] = 17
shark = [0, 0, fishes[start][3]]
fishes[start][0] = 0

dfs(0, 0, fishes[start][3], start, 1)
print(answer)




