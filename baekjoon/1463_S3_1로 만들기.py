N = int(input())

DP = [0] * (3 * N + 1)

DP[0] = 1
DP[1] = 1
DP[2] = 1
DP[3] = 1
for i in range(2, N + 1, 1):
    if DP[i * 3]:
        DP[i * 3] = min(DP[i * 3], DP[i] + 1)
    else:
        DP[i * 3] = DP[i] + 1

    if DP[i * 2]:
        DP[i * 2] = min(DP[i * 2], DP[i] + 1)
    else:
        DP[i * 2] = DP[i] + 1

    if DP[i + 1]:
        DP[i + 1] = min(DP[i + 1], DP[i] + 1)
    else:
        DP[i + 1] = DP[i] + 1

if N == 1:
    print(0)
else:
    print(DP[N])


