def dfs(r: int, c: int, cnt: int, chance: float) -> None:
    global answer

    if cnt == n:
        answer += chance
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, cnt + 1, chance * percentage[i])
            visited[nr][nc] = 0


n, E, W, S, N = map(int, input().split())
percentage = [E / 100, W / 100, S / 100, N / 100]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
visited = [[0 for _ in range(30)] for _ in range(30)]
answer = 0
visited[14][14] = 1
dfs(14, 14, 0, 1)

print(round(answer, 9))










