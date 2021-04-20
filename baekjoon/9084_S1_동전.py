import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())
    memo = [0] * (amount + 1)
    memo[0] = 1
    for i in range(N):
        for j in range(coins[i], amount+1):
            memo[j] += memo[j - coins[i]]
    print(memo[-1])







