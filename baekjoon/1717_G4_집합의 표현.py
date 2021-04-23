import sys
sys.stdin = open("input.txt", "r")

def find(x):
    temp = x
    while p[x] != x:
        x = p[x]
    # 부모를 루트로 변경
    p[temp] = x
    return x

def union(x, y):
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        p[root2] = root1

N, M = map(int, input().split())
p = list(range(N+1))

for _ in range(M):
    op, x, y = map(int, input().split())
    if op:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')
    else:
        union(x, y)




