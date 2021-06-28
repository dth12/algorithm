import sys
input = sys.stdin.readline

memo = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(91):
    memo.append(memo[-1] + memo[-5])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(memo[N])



