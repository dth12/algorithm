from itertools import permutations
from collections import deque

# ctrl과 함께 눌렀을 때, 찾기.
def ctrl(r: int, c: int, dr: int, dc: int, copy:list):
    
    while True:
        r += dr
        c += dc
        
        if not (0 <= r < 4 and 0 <= c < 4):
            return r - dr, c - dc
        
        if copy[r][c]:
            return r, c


# bfs로 최단거리 찾기.
def bfs(start: list, copy: list, end: list):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = deque([start])
    visited = [[0 for _ in range(4)] for _ in range(4)]
    time = 0
    while Q:
        L = len(Q)
        time += 1
        for _ in range(L):
            r, c = Q.popleft()
            visited[r][c] = 1
            if [r, c] == end: return time 
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    ctrl_r, ctrl_c = ctrl(r, c, dr[i], dc[i], copy)

                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        Q.append([nr ,nc])

                    if not visited[ctrl_r][ctrl_c]:
                        visited[ctrl_r][ctrl_c] = 1
                        Q.append([ctrl_r, ctrl_c])
            

def solution(board, R, C):
    global min_value, min_pos
    answer = 100
    selected = []
    pos = {}
    for r in range(4):
        for c in range(4):
            if board[r][c]:
                if not board[r][c] in selected:
                    selected.append(board[r][c])    
                if board[r][c] in pos:
                    pos[board[r][c]].append([r, c])
                else:
                    pos[board[r][c]] = [[r, c]]
    
    # 모든 케이스를 발생시켜서 누구부터 터트릴지 결정.  
    for case in permutations(selected, len(selected)):
        copy = [[board[r][c] for c in range(4)] for r in range(4)]
        temp = 0
        sr = R
        sc = C

        for target in case:
            # A to B를 거쳐서 찾기와 B to A를 거쳐서 찾기 중 누가 더 빠른지 결정.
            temp1 = 0
            temp2 = 0
            r1, c1 = pos[target][0]
            r2, c2 = pos[target][1]
            
            temp1 += bfs([sr, sc], copy, [r1, c1])
            copy[r1][c1] = 0
            temp1 += bfs([r1, c1], copy, [r2, c2])
            copy[r1][c1] = 1
            
            temp2 += bfs([sr, sc], copy, [r2, c2])
            copy[r2][c2] = 0
            temp2 += bfs([r2, c2], copy, [r1, c1])
            copy[r1][c1] = 0
            if temp1 > temp2:
                sr, sc = r1, c1
                temp += temp2
            else:
                sr, sc = r2, c2
                temp += temp1
        
        answer = min(temp, answer)
            
    return answer