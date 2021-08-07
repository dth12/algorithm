N = int(input())
arr = list(map(int, input().split()))

memo = [0 for _ in range(N)]
memo[0] = arr[0]

for i in range(1, N):
    if memo[i - 1] + arr[i] > arr[i]:
        memo[i] = arr[i] + memo[i - 1]
    else:
        memo[i] = arr[i]

print(max(memo))


