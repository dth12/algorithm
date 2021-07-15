import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    blank = input()
    n, k = map(int, input().split())
    land = [-1] * n
    pos = list(map(int, input().split()))
    temper = list(map(int, input().split()))

    for i in range(k):
        land[pos[i] - 1] = temper[i]

    for i in range(n):
        min_val = 1000000000000
        for j in range(k):
            if min_val > (temper[j] + abs(i - pos[j] + 1)):
                min_val = temper[j] + abs(i - pos[j] + 1)

        land[i] = min_val
    print(*land)