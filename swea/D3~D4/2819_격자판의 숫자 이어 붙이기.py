def dfs(r:int, c:int, length:int, num:str) -> None:
    if length == 7:
        cases.add(num)
        return
    else:
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, length+1, num + grid[r][c])


for tc in range(1, int(input())+1):
    grid = [list(input().split()) for _ in range(4)]
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    cases = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, 0, '')

    print('#{} {}'.format(tc, len(cases)))

