import sys
sys.stdin = open("input.txt", "r")


def dfs(total, idx):
    global MIN

    if total > MIN:
        return

    if idx == N:
        MIN = min(total, MIN)

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(total+factories[idx][i], idx+1)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    MIN = 10000000000000
    factories = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    dfs(0, 0)
    print('#{} {}'.format(tc, MIN))