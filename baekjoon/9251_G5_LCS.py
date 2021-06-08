import sys
input = sys.stdin.readline

A = list(input())
B = list(input())

DP = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        DP[i][]
