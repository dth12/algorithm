import sys
sys.stdin = open("input.txt", "r")

def b_to_d(num:list) -> int:
    L = len(num) - 1
    val = 0
    idx = 0
    while L >= 0:
        val += num[idx] * (2**L)
        idx += 1
        L -= 1
    return val

def t_to_d(num:list) -> int:
    L = len(num) - 1
    val = 0
    idx = 0
    while L >= 0:
        val += num[idx] * (3**L)
        idx += 1
        L -= 1
    return val


def find() -> int:
    t = t_to_d(ternary)
    b = b_to_d(binary)
    # 한자리씩 변경했을 때, 가능한 모든 값을 저장합니다. - 2진수
    bin = set()
    L = len(binary)
    for i in range(L):
        if binary[i] == 0:
            bin.add(2 ** (L - i - 1))
        elif binary[i] == 1:
            bin.add(-(2 ** (L - i - 1)))

    # 한자리씩 변경했을 때, 가능한 모든 값을 저장합니다. - 3진수
    ter = set()
    L = len(ternary)
    for i in range(L):
        for j in range(ternary[i]):
            ter.add(-(j+1) * 3 ** (L - i - 1))
        for j in range(1, 3-ternary[i]):
            ter.add(j * 3 ** (L - i - 1))

    # 가능한 값들을 원래 값에 더했을 때, 같으면 return 해줍니다.
    for i in bin:
        for j in ter:
            if b + i == t + j:
                if b + i >= 0:
                    return b + i


for tc in range(1, int(input())+1):
    binary = list(map(int, input()))
    ternary = list(map(int, input()))
    print('#{} {}'.format(tc, find()))