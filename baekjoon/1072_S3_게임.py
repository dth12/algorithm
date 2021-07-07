'''
    실수 계산 꼭 신경쓰자.
'''
X, Y = map(int, input().split())
Z = Y * 100 // X
answer = -1
if Z < 99:
    start = 0
    end = 1000000000
    mid = (end + start) // 2
    while start <= end:
        mid = (end + start) // 2
        win_rate = 100 * (mid + Y) // (mid + X)
        if win_rate > Z:
            end = mid - 1
            answer = mid
        elif win_rate <= Z:
            start = mid + 1

print(answer)



