import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
memo = [0 for _ in range(N)]

for i in range(N):
    if not memo[i]:
        memo[i] = 1
    for j in range(i, N):
        if arr[i] < arr[j]:
            memo[j] = max(memo[i] + 1, memo[j])

print(max(memo))

