N = int(input())
DP = [-1] * (2 * N + 1)

idx = 1
for i in range(3, N + 1, 3):
    DP[i] = idx
    idx += 1

idx = 1
for i in range(5, N + 1, 5):
    DP[i] = idx
    idx += 1


for num1 in range(3, N + 1, 3):
    if DP[num1] == -1: continue
    for num2 in range(5, N + 1, 5):
        if DP[num2] > 0:
            if DP[num1 + num2] == -1:
                DP[num1 + num2] = DP[num1] + DP[num2]
            else:
                DP[num1 + num2] = min(DP[num1] + DP[num2], DP[num1 + num2])

print(DP[N])




