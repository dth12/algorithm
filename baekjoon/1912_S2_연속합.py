N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(max(0, arr[0]))
else:
    last = 0
    max_val = 0
    total = 0
    for i in range(N):
        if arr[last] <

