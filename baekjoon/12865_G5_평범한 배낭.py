N, limit = map(int, input().split())

memo = [0] * (limit + 1)
for _ in range(N):
    weight, value = map(int, input().split())

    for i in range(limit, weight - 1, -1):
        memo[i] = max(memo[i - weight] + value, memo[i])

print(memo[limit])


