import sys
input = sys.stdin.readline


def init(start: int, end: int, node: int):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid+1, end, node * 2 + 1)
    return tree[node]


def update_lazy(start: int, end: int, node: int):
    if lazy[node]:
        tree[node] += lazy[node] * (end - start + 1)
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0


def update(start: int, end: int, node: int, left: int, right: int, diff: int):
    update_lazy(start, end, node)
    if start > right or end < left:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, left, right, diff)
    update(mid+1, end, node * 2 + 1, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]


def partial_sum(start: int, end: int, node: int, left: int, right: int):
    update_lazy(start, end, node)
    if left <= start and end <= right:
        return tree[node]

    if start > right or end < left:
        return 0

    mid = (start + end) // 2
    return partial_sum(start, mid, node * 2, left, right) + partial_sum(mid+1, end, node * 2 + 1, left, right)


N, M, K = map(int, input().split())
arr = [0] * (N+1)
tree = [0] * (N * 4)
lazy = [0] * (N * 4)
for i in range(1, N+1):
    arr[i] = int(input())

init(1, N, 1)
for _ in range(M+K):
    command = list(map(int, input().split()))
    if command[0] == 1:
        update(1, N, 1, command[1], command[2], command[3])
    elif command[0] == 2:
        print(partial_sum(1, N, 1, command[1], command[2]))
