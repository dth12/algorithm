import sys
sys.stdin = open("input.txt", "r")

def dfs(cnt, idx):
    global MIN

    if idx == K:
        MIN = min(MIN, cnt)
        return

    if cnt > MIN:
        return

    if orders[idx] in plug:
        dfs(cnt, idx+1)
    elif len(plug) < N:
        plug.append(orders[idx])
        dfs(cnt, idx+1)
    elif len(plug) >= N:
        for i in range(N):
            temp = plug[i]
            plug[i] = orders[idx]
            dfs(cnt + 1, idx + 1)
            plug[i] = temp


MIN = 1000
N, K = map(int, input().split())
orders = list(map(int, input().split()))
plug = []

dfs(0, 0)
print(MIN)


