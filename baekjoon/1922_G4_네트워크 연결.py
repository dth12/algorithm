import sys
sys.stdin = open("input.txt", "r")

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    p[x] = y


N = int(input())
M = int(input())
p = list(range(N+1))
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
answer = 0
cnt = 0

for x, y, cost in edges:
    if cnt == N-1:
        break
    r1 = find(x)
    r2 = find(y)

    if r1 != r2:
        answer += cost
        union(r1, r2)
        cnt += 1

print(answer)


