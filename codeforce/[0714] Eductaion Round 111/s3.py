import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    answer = 0
    N = int(input())
    arr = list(map(int, input().split()))
    answer += N + (N - 1)
    for i in range()