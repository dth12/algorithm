import sys
sys.stdin = open('input.txt', 'r')

def inrange(idx: int, N: int):
    return 0 <= idx < N


def solve(word: str) -> str:
    include_set = set()
    next_code = ord('a') + 1
    N = len(word)
    idx = -1

    for i in range(len(word)):
        if word[i] in include_set:
            return 'NO'
        else:
            include_set.add(word[i])

        if word[i] == 'a':
            idx = i

    if idx == -1:
        return 'NO'

    while True:
        if len(word) == 1:
            return 'YES'
        else:
            if inrange(idx - 1, len(word)) and ord(word[idx - 1]) == next_code:
                idx -= 1
                next_code += 1
                word = word[:idx] + word[idx + 1:]
            elif inrange(idx + 1, len(word)) and ord(word[idx + 1]) == next_code:
                next_code += 1
                word = word[:idx] + word[idx + 1:]
            else:
                return 'NO'


T = int(input())
for tc in range(1, T + 1):
    word = input()
    print(solve(word))

