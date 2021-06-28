import sys
input = sys.stdin.readline
A = list(input())
B = list(input())

A.pop()
B.pop()

memo = [[0 for _ in range(len(A))] for _ in range(len(B))]


flag = 0
for j in range(len(A)):
    if flag == 0 and A[0] == B[j]:
        flag = 1
        memo[0][j] = 1
    elif flag:
        memo[0][j] = 1

for i in range(1, len(B)):
    b = B[i]
    if i == 2:
        debug = True
    for j in range(len(A)):
        a = A[j]
        if a == b:
            if memo[i - 1][j] <= j:
                memo[i][j] = memo[i - 1][j] + 1
            else:
                memo[i][j] = memo[i - 1][j] + 1
        elif a != b:
            if j == 0:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])

print(max(max(memo)))



