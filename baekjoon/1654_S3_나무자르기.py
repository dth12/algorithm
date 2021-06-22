import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
flag = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for h in tree:
        total += (h - mid) if h > mid else 0

    if total >= M:
        start = mid + 1
    elif total < M:
        end = mid - 1


print(end)

