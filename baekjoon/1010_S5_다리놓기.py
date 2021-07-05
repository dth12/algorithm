T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    if N == M:
        print(1)
    else:
        numerator = 1
        denominator = 1

        for i in range(M, M - N, -1):
            numerator *= i

        for i in range(1, N + 1):
            denominator *= i

        print(numerator//denominator)
