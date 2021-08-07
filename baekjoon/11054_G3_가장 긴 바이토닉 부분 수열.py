N = int(input())
arr = list(map(int, input().split()))

memo_inc = [0 for _ in range(N)]
memo_dec = [0 for _ in range(N)]
for i in range(N):
    if memo_inc[i] == 0:
        memo_inc[i] = 1

    for j in range(i + 1, N):
        if arr[i] < arr[j]:
            memo_inc[j] = max(memo_inc[i] + 1, memo_inc[j])

for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if arr[i] < arr[j]:
            memo_dec[j] = max(memo_dec[i] + 1, memo_dec[j])

max_val = 0
for i in range(N):
    if max_val < memo_dec[i] + memo_inc[i]:
        max_val = memo_dec[i] + memo_inc[i]

print(max_val)
