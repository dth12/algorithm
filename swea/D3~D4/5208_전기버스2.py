import sys
sys.stdin = open("input.txt", "r")


def dfs(idx, cnt):
    global MIN

    if cnt > MIN:
        return

    if idx + stops[idx] >= N:
        MIN = min(MIN, cnt)
        return

    for i in range(idx+1, min(stops[idx]+idx+1, len(stops))):
            dfs(i, cnt+1)


for tc in range(1, int(input())+1):
    stops = list(map(int, input().split()))
    N = stops[0]
    MIN = len(stops)
    dfs(1, 0)
    print('#{} {}'.format(tc, MIN))