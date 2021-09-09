def solution(grid):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    R = len(grid)
    C = len(grid[0])
    answer = []
    visited = [[[[0, 0] for _ in range(4)] for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):
            for i in range(4):
                o = i  # 방향
                l = 0  # 길이
                r = row
                c = col
                nr = r + dr[o]
                nc = c + dc[o]
                if nr == R: nr = 0
                if nr < 0: nr = R - 1
                if nc == C: nc = 0
                if nc < 0: nc = C - 1

                while visited[nr][nc][o][0] == 0 and visited[r][c][o][1] == 0:
                    visited[nr][nc][o][0] = 1
                    visited[r][c][o][1] = 1

                    if grid[nr][nc] == 'L':
                        o -= 1
                        if o < 0: o = o + 4
                    elif grid[nr][nc] == 'R':
                        o += 1
                        if o == 4: o = 0

                    l += 1
                    r = nr
                    c = nc
                    nr += dr[o]
                    nc += dc[o]
                    if nr == R: nr = 0
                    if nr < 0: nr = R - 1
                    if nc == C: nc = 0
                    if nc < 0: nc = C - 1

                if l:
                    answer.append(l)

    answer.sort()
    return answer


print(solution(["R","R"]))