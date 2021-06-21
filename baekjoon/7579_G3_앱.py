import sys
input = sys.stdin.readline
N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
total = sum(memories)
cost_sum = sum(costs)
memo = [cost_sum] * (total + 1)


for i in range(N):
    for j in range(M, total + 1 - memories[i]):
        memo[j] = min(memo[j + memories[i]] - costs[i], memo[j])

print(min(memo))







