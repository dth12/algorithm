import sys
sys.stdin = open('input.txt', 'r')

from math import ceil, sqrt
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(ceil(sqrt(N)))