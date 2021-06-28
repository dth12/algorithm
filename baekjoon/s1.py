import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if arr[i] >= i + 1:
            start = arr[i]
        else:
            start = ((i + 1) // arr[i] + 1) * arr[i]
        for j in range(start, N, arr[i]):
            if arr[i] * arr[j] == i + j + 2:
                cnt += 1

    print(cnt)



