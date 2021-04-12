# 전형적인 DP 문제
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        b = 1
        a = 2
        for _ in range(2, n):
            c = a + b
            b = a
            a = c

    return c % 1000000007