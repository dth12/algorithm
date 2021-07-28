import sys
input = sys.stdin.readline

T = list(input().strip())
P = list(input().strip())
KMP = [0 for _ in range(len(P))]
for i in range(1, len(P)):
    if P[i - 1] == P[KMP[i - 1]]:
        KMP[i] = KMP[i - 1] + 1
    else:
        KMP[i] = KMP[i - 1]

answer = 0
flag = 0
start_T = 0
start_P = 0

while True:
    if start_T >= len(T) - len(P):
        break

    for i in range(start_P, len(P)):
        if T[start_T + i] != P[i]:
            if KMP[i]:
                if i - KMP[i]:
                    start_T += i - KMP[i]
                else:
                    start_T += 1
                start_P = KMP[i]
            else:
                start_T += i + 1
                start_P = 0
            flag = 1
            break

    if flag:
        flag = 0
        continue

    answer += 1
    start_P = KMP[-1]
    start_T += len(P) - KMP[-1]


print(answer)
'''
ABCDABCDABDE
ABCDABD
            A B C D A B D
    
    1 1 1 1 1 2 3
'''