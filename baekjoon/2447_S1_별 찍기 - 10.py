def drawing(row: int, col: int, edge: int):
    if edge == 1:
        board[row][col] = '*'
    else:
        edge //= 3
        for r in range(3):
            for c in range(3):
                if r != 1 or c != 1:
                    drawing(row + edge * r, col + edge * c, edge)


N = int(input())
board = [[' ' for _ in range(N)] for _ in range(N)]
drawing(0, 0, N)

for i in board:
    print(''.join(i))




