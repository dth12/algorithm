from math import log2, ceil
import sys
input = sys.stdin.readline


def make_segment_tree(start: int, end: int, node: int) -> int:
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        left = make_segment_tree(start, mid, node * 2)
        right = make_segment_tree(mid + 1, end, node * 2 + 1)
        tree[node] = left + right
        return tree[node]


def calc_parital_sum(left: int, right: int, start: int, end: int, node: int) -> int:
    if left <= start and end <= right: # 완전히 포함됨
        return tree[node]

    if (start <= right <= end) or (start <= left <= end): # 일부분만 포함됨
        mid = (start + end) // 2
        left_sum = calc_parital_sum(left, right, start, mid, node * 2) # 왼쪽
        right_sum = calc_parital_sum(left, right, mid + 1, end, node * 2 + 1) # 오른쪽
        return left_sum + right_sum

    return 0 # 어느 부분도 포함되지 않음 탐색 종료


def update_segment_tree(idx: int, diff: int, start: int, end: int, node: int) -> None:
    if start <= idx <= end: # 포함될 때.
        mid = (start + end) // 2
        tree[node] += diff # 트리 업데이트
        if start != end: # 리프 노드가 아닐 때 진입
            update_segment_tree(idx, diff, start, mid, node * 2)
            update_segment_tree(idx, diff, mid + 1, end, node * 2 + 1)


N, M, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))


exp = ceil(log2(len(arr))) + 1
tree = [0 for _ in range(2**exp)]
make_segment_tree(0, len(arr) - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1

    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update_segment_tree(b, diff, 0, len(arr) - 1, 1)
    else:
        print(calc_parital_sum(b, c - 1, 0, len(arr) - 1, 1))

