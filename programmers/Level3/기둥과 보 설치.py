# 0 기둥 1 보, 0 삭제 1 설치
def is_bo_built(r, c, grid, n):
    if grid[r-1][c][0] or grid[r-1][c+1][0]: # 양쪽 하나라도 기둥이 받쳐주면.
        return True
    elif 0 < c < n-1 and grid[r][c-1][1] and grid[r][c+1][1]:
        return True
    
    return False


def is_col_built(r, c, grid, n):
    if r == 0:
        return True
    elif 0 < r <= n - 1:
        if grid[r][c][1]: # 보가 기둥이 세워지는 위치에 있을 때
            return True
        elif grid[r-1][c][0]: # 기둥이 세워지는 위치에 기둥이 있을 때
            return True
        elif 0 < c and grid[r][c-1][1]:
            return True
    
    return False

        
def is_stable(r, c, grid, build, n):
    grid[r][c][build] = 0
    for row in range(n+1):
        for col in range(n+1):
            if grid[row][col][0] and not is_col_built(row, col, grid, n):
                return False
            if grid[row][col][1] and not is_bo_built(row, col, grid, n):
                return False
            
    return True
                

def solution(n, build_frame):
    answer = []
    grid = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

    for c, r, build, is_built in build_frame:
        if build: # 보
            if is_built: # 설치
                if is_bo_built(r, c, grid, n):
                    grid[r][c][build] = 1
            else: # 삭제
                if not is_stable(r, c, grid, build, n):
                    grid[r][c][build] = 1
        else: # 기둥
            if is_built:
                if is_col_built(r, c, grid, n):
                    grid[r][c][build] = 1
            else:
                if not is_stable(r, c, grid, build, n):
                    grid[r][c][build] = 1
    
    for r in range(n+1):
        for c in range(n+1):
            if grid[r][c][0]:
                answer.append([c, r, 0])
            if grid[r][c][1]:
                answer.append([c, r, 1])
    
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer