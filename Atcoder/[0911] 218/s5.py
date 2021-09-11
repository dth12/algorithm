import sys
sys.setrecursionlimit(100000)


def find(a: int) -> int:
    if tree[a] == a:
        return a
    else:
        b = tree[a]
        tree[a] = find(b)
        return tree[a]


def union(a: int, b: int) -> None:
    if rank[a] < rank[b]:
        tree[a] = b
    else:
        tree[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key=lambda x: x[2])
tree = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]

val = 0
cnt = 0
for a, b, c in graph:
    if cnt < N - 1:
        pa = find(a)
        pb = find(b)
        if pa != pb:
            union(pa, pb)
            cnt += 1
        else:
            if c >= 0: val += c
    else:
        if c >= 0: val += c

print(val)
