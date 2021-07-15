T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    prefix = '0b'
    answer = [0]

    if len(numbers) == 1:
        print(*answer)
    else:
        for i in range(1, len(numbers)):
            before = numbers[i - 1] ^ answer[i - 1]
            answer.append(before & (~numbers[i]))

        print(*answer)