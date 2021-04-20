import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, prob):
    global MAX

    if prob <= 0.000000000001:
        return

    if prob - MAX < 0:
        return

    if idx == N:
        MAX = max(prob, MAX)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, prob*graph[idx][i]/100)
            visited[i] = 0


for tc in range(1, int(input())+1):
    # 1 <= N <= 16
    N = int(input())
    MAX = 0
    graph = [list(map(float, input().split())) for _ in range(N)]
    visited = [0] * N
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, MAX*100))