def solution(w, h, puddles):
    grid = [[0 for _ in range(w)] for _ in range(h)]
    grid[0][0] = 1
    
    for r in range(h):
        for c in range(w):
            if [c + 1, r + 1] in puddles: continue
            if 0 <= r-1:
                grid[r][c] += grid[r - 1][c] 
            if 0 <= c-1:  
                grid[r][c] += grid[r][c - 1]
            
    return grid[h-1][w-1] % 1000000007