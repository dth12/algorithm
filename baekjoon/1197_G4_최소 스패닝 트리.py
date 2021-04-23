import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    p[x] = y

V, E = map(int, input().split())
p = list(range(0, V+1))
answer = 0
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

for v1, v2, w in edges:
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        answer += w
        union(r1, r2)



V, E = map(int, input().split())





print(answer)













