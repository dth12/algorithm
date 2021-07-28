import sys
input = sys.stdin.readline

def is_right(r: int, c: int) -> bool:
    k = (r // 3) * 3 + (c // 3)
    if board[r][c] in visited_row[c]: return False
    if board[r][c] in visited_col[r]: return False
    if board[r][c] in visited_box[k]: return False

    visited_row[c].add(board[r][c])
    visited_col[r].add(board[r][c])
    visited_box[k].add(board[r][c])
    return True


def dfs(idx: int) -> None:
    global flag

    if idx == len(empty):
        flag = 1
        return

    r, c = empty[idx]
    for i in range(1, 10):
        board[r][c] = i
        if is_right(r, c):
            dfs(idx + 1)
            k = (r // 3) * 3 + (c // 3)
            visited_row[c].remove(board[r][c])
            visited_col[r].remove(board[r][c])
            visited_box[k].remove(board[r][c])
        if flag:
            return

    board[r][c] = 0


board = [list(map(int, input().split())) for _ in range(9)]
visited_row = [set() for _ in range(9)]
visited_col = [set() for _ in range(9)]
visited_box = [set() for _ in range(9)]

empty = []
flag = 0

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            empty.append([r, c])
        else:
            i = (r // 3) * 3 + (c // 3)
            visited_row[c].add(board[r][c])
            visited_col[r].add(board[r][c])
            visited_box[i].add(board[r][c])

dfs(0)
for row in board:
    print(*row)

