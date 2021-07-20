N, K = map(int, input().split())

denom1 = 1
denom2 = 1
num = 1

for i in range(1, N + 1):
    num *= i
    num %= 1000000007
    if i == K:
        denom1 = num

    if i == (N - K):
        denom2 = num

print(num // (denom1 * denom2))


