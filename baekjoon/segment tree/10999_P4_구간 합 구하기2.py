import sys
input = sys.stdin.readline

def init(start: int, end: int, node: int):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid+1, end, node * 2 + 1)
    return tree[node]


def update(start: int, end: int, node: int, left: int, right: int, diff: int):
    if start <= left and right <= end:
        tree[node] += (right - left + 1) * diff + lazy[node]
        lazy[node * 2] += (right - left + 1) * diff + lazy[node]
        lazy[node * 2 + 1] += (right - left + 1) * diff + lazy[node]
        lazy[node] = 0
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node * 2, index, diff)
            update(mid+1, end, node * 2 + 1, index, diff)


def partial_sum(start: int, end: int, node: int, left: int, right: int):
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
        command[1]

    elif command[0] == 2:
        print(partial_sum(1, N, 1, command[1], command[2]))
