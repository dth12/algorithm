import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(input())
    numbers_set = set()
    T = N // 4
    for _ in range(len(num)):
        for i in range(T, len(num), T):
            N = ''.join(num[i-T:i])
            numbers_set.add(int(N, 16))

        num = [num.pop()] + num

    numbers = list(numbers_set)
    numbers.sort(reverse=True)
    print('#{} {}'.format(tc, numbers[K-1]))




