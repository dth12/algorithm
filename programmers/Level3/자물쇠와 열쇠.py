def solution(key, lock):
    # 완전히 감쌀 수 있는 초대형 list 생성
    N = len(lock)
    M = len(key)
    stack = []
    holes = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                stack.append([i, j])
                
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                holes.append([i, j])
    # 23 25 33
    if holes == []:
        return True
    
    for _ in range(4):
        for hole in holes:
            r = hole[0]
            c = hole[1]
            for i in stack:
                key_r = i[0]
                key_c = i[1]
                dr = r - key_r 
                dc = c - key_c
                cnt = 0
                for j in stack:
                    nr = dr + j[0]
                    nc = dc + j[1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if lock[nr][nc] == 1:
                            cnt = -1
                            break
                        elif lock[nr][nc] == 0:
                            cnt += 1
                            
                if cnt == len(holes):
                    return True
                    
        holes = []
        lock = [list(i)[::-1] for i in zip(*lock)]
        for i in range(N):
            for j in range(N):
                if lock[i][j] == 0:
                    holes.append([i, j])
        
    return False