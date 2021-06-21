import sys
input = sys.stdin.readline
N, limit = map(int, input().split())
memo = [0] * (limit + 1)

for _ in range(N):
    weight, value, count = map(int, input().split())
    for repeat in range(count):
        for i in range(limit, weight + weight * repeat - 1, -1):
            memo[i] = max(memo[i - weight] + value, memo[i])

print(max(memo))
