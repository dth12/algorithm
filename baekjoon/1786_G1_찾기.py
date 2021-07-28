import sys
input = sys.stdin.readline


def KMP_init() -> None:
    i = 0
    j = 1
    while j < len(P):
        if P[i] == P[j]:
            i += 1
            KMP[j] = i
        else:
            while i > 0 and P[i] != P[j]:
                i = KMP[i - 1]

            if P[i] == P[j]:
                i += 1
                KMP[j] = i

        j += 1


T = list(input()) # target
P = list(input()) # pattern
answer = 0
pos = []
KMP = [0 for _ in range(len(P))]
KMP_init()

i = 0
j = 0
while j < len(T):
    if P[i] == T[j]:
        i += 1
    else:
        while i > 0 and P[i] != T[j]:
            i = KMP[i - 1]

        if P[i] == T[j]:
            i += 1

    if i == len(P):
        pos.append(j + 2 - len(P))
        answer += 1
        i = KMP[-1]

    j += 1

print(answer)
print(*pos)





