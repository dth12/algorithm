import sys
from math import log, ceil
input = sys.stdin.readline


def init(start: int, end: int, node: int):

    if start == end:
        tree[node] = [info[start], info[start]]
        return [info[start], info[start]]
    else:
        mid = (start + end) // 2
        left = init(start, mid, node * 2)
        right = init(mid+1, end, node * 2 + 1)
        if left[1] >= right[1]:
            area = (end - start + 1) * right[1]
            tree[node] = [area, right[1]]
            return tree[node]
        else:
            area = (end - start + 1) * left[1]
            tree[node] = [area, left[1]]
            return tree[node]

def total(start: int, end:int ,left: int, right: int, node: int):

    # 완전히 포함될 때,
    if left <= start and right <= end:
        return tree[node]

    # 포함이 되지 않을 때,
    if left > start or right > end:
        return [0, 0]

    # 아니라면 재탐색
    mid = (start + end) // 2
    a = total(start, mid, left, right, node * 2)
    b = total(mid + 1, end, left, right, node * 2 + 1)
    if a[1] >= b[1]:
        return [(end - start + 1) * b[1], b[1]]
    else:
        return [(end - start + 1) * a[1], a[1]]


while True:
    info = list(map(int, input().split()))
    if info[0] == 0:
        break

    N = info[0]

    size = 1 << (ceil(log(N, 2)) + 1)
    # 0번 => 직사각형 크기, 1번 => 내 높이
    tree = [[0, 0] for _ in range(size+1)]
    init(1, N, 1)
    print(total(1, N, 1, 4, 1))







