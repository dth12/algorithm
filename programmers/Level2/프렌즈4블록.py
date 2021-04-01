def solution(m, n, board):
    
    for i in range(len(board)):
        board[i] = list(board[i])

    answer = 0
    stack = [[1, 1]]
    while stack:
        stack = []
        for r in range(1, m):
            for c in range(1, n):
                if board[r][c] != 0:
                    doll = board[r][c]
                    if board[r-1][c] == doll and board[r][c-1] == doll and board[r-1][c-1] == doll:
                        stack.append([r, c])
        
        for pos in stack:
            nr = pos[0]
            nc = pos[1]
            if board[nr-1][nc] != 0:
                board[nr-1][nc] = 0
                answer += 1
            if board[nr][nc] != 0:
                board[nr][nc] = 0
                answer += 1
            if board[nr][nc-1] != 0:
                board[nr][nc-1] = 0
                answer += 1
            if board[nr-1][nc-1] != 0:
                board[nr-1][nc-1] = 0
                answer += 1

        for col in range(n):
            temp = []
            for row in range(m):
                if board[row][col] != 0:
                    temp.append(board[row][col])
                else:
                    for i in range(len(temp)):
                        board[row-i][col] = temp[len(temp)-1-i]
                        board[row-i-1][col] = 0
            
    return answer