import sys
sys.stdin = open("input.txt", "r")

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 != root2:
        p[root1] = root2
    else:
        return True


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    p = list(range(0, N + 1))
    answer = 0

    for i in range(M):
        x = temp[i*2]
        y = temp[i*2+1]
        union(x, y)

    for i in range(1, N+1):
        if p[i] == i:
            answer += 1

    print('#{} {}'.format(tc, answer))





