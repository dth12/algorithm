def mix(repeat):
    global MAX
    if repeat == K:
        temp = int(''.join(num))
        MAX = max(temp, MAX)
        return
    else:
        for i in range(N):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                mix(repeat+1)
                num[i], num[j] = num[j], num[i]

T = int(input())

for tc in range(1, T+1):
    num, K = input().split()
    K = int(K)
    num = list(num)
    N = len(num)
    MAX = 0
    # K가 N-1보다 크면 의미가 없어짐.
    # N-1보다 작아질 때까지 계속 -2씩 빼줌
    if N-1 < K:
        while N-1 < K:
            K -= 2
    mix(0)

    print('#{} {}'.format(tc, MAX))






