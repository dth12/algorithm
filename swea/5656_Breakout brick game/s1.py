import sys
from copy import deepcopy
import timeit
from pandas import DataFrame as df
sys.stdin = open("input.txt", "r")


# 벽돌을 깨주는 함수입니다.
def crash(board, r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = [[r, c, board[r][c]]]

    # bfs처럼 주위에 있는 모든 벽돌을 깬 후, 크기가 2이상인 블럭만 queue에 담아줍니다.
    while queue:
        v = queue.pop(0)
        nr = v[0]
        nc = v[1]
        x = v[2]
        board[nr][nc] = 0

        for i in range(4):
            repeat = 1
            nr = v[0]
            nc = v[1]

            while repeat < x and 0 <= nr + dr[i] < H and 0 <= nc + dc[i] < W:
                nr += dr[i]
                nc += dc[i]

                if board[nr][nc] == 1:
                    board[nr][nc] = 0
                elif board[nr][nc] > 1:
                    queue.append([nr, nc, board[nr][nc]])
                    board[nr][nc] = 0

                repeat += 1


def inspect():
    global min_value
    bricks_copy = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            bricks_copy[i][j] = bricks[i][j]
    result = 0

    for c in sel:
        for r in range(H):

            if bricks_copy[r][c] > 0:
                nr = r
                nc = c
                crash(bricks_copy, nr, nc)
                # 벽돌을 밑으로 내리는 과정입니다
                # stack에 1이상인 값들을 넣어주고, 밑에서부터 위로 차례대로 바꿔줍니다.

                for col in range(W):
                    row = 0
                    stack = []

                    while row < H:
                        if bricks_copy[row][col] > 0:
                            stack.append(bricks_copy[row][col])
                        else:
                            idx = len(stack) - 1
                            move = 0

                            while idx >= 0:
                                bricks_copy[row - move][col] = stack[idx]
                                bricks_copy[row - move - 1][col] = 0
                                idx -= 1
                                move += 1

                        row += 1
                break

    for i in range(H):
        for j in range(W):
            if bricks_copy[i][j] > 0:
                result += 1

    return result

# 모든 경우의 수를 판별하여 순열을 만들어줍니다.
def permutation(idx):
    global min_value

    # 만약 min_value가 이미 0이라면 끝내줍니다.
    if min_value == 0:
        return

    if idx == N:
        min_value = min(inspect(), min_value)
        return

    # 모든 경우의 수를 발생시킵니다.
    for i in range(W):
        if check[i] > 0:
            sel[idx] = num[i]
            check[i] -= 1
            permutation(idx + 1)
            check[i] += 1


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    min_value = 10000000000
    bricks = [list(map(int, input().split())) for _ in range(H)]
    num = list(range(0, W))
    sel = [W-1] * N
    check = [N] * W
    permutation(0)
    print('#{} {}'.format(tc, min_value))