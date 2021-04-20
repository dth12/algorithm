def dfs(idx, total, n):
    global answer
    if idx == N:
        if visited[total] == 0:
            answer += 1
            visited[total] = 1
        return
    for i in range(n, 4):
        dfs(idx+1, total+num[i], i)

N = 20
answer = 0
visited = [0] * 1001
num = [1, 5, 10, 50]
dfs(0, 0, 0)
print(answer)