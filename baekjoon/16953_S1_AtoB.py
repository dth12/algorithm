import sys
sys.stdin = open("input.txt", "r")

A, B = map(int, input().split())
answer = 1
while A != B:
    if str(B)[-1] == '1':
        B = int(str(B)[:len(str(B))-1])
        answer += 1
    elif B % 2 == 0:
        B //= 2
        answer += 1
    elif B % 2 == 1:
        answer = -1
        break

    if B < A:
        answer = -1
        break

print(answer)



