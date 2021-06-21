import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)



def set_parent(node: int):
    for i in arr[node]:
        if tree[i] == -1:
            tree[i] = node
            set_parent(i)


N = int(input())
arr = [[] for _ in range(N + 1)]
tree = [ -1 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

set_parent(1)
for i in range(2, N + 1):
    print(tree[i])
