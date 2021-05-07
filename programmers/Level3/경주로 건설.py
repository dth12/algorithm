from collections import deque
def inrange(r, c, N):
    return 0 <= r < N and 0 <= c < N

def solution(board):
    dist = [[10000000 for _ in range(len(board))] for _ in range(len(board))]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    Q = deque([[0, 0, -1, 0]])
    dist[0][0] = 0
    while Q:
        r, c, before, total = Q.popleft()
        if dist[r][c] > total:
            dist[r][c] = total
        elif dist[r][c] < total:
            continue
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc, len(board)) and not board[nr][nc]:
                if before == i or before == -1:
                    if total + 100 <= dist[nr][nc]:
                        Q.append([nr, nc, i, total+100])
                else:
                    if total + 600 <= dist[nr][nc]:
                        Q.append([nr, nc, i, total+600])

    return dist[len(board)-1][len(board)-1]