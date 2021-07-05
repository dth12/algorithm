def dfs(cnt: int, repeat: int, total: int):
    global max_val

    if cnt == N - 1 and repeat == 1:
        return

    if total < memo[cnt][repeat]:
        return

    memo[cnt][repeat] = total
    max_val = max(max_val, total)

    if cnt >= N:
        return

    if cnt + 2 <= N:
        dfs(cnt + 2, 0, total + stair[cnt + 2])

    if cnt + 1 <= N and repeat == 0:
        if cnt == 0:
            dfs(cnt + 1, 0, total + stair[cnt + 1])
        else:
            dfs(cnt + 1, 1, total + stair[cnt + 1])


N = int(input())
stair = [int(input()) for _ in range(N)]
stair = [0] + stair
max_val = 0
memo = [[0 for _ in range(2)] for _ in range(N + 1)]
dfs(0, 0, 0)
print(max_val)
