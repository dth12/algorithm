import sys
sys.stdin = open("input.txt", "r")

S = input()
T = input()
result = 1

while S != T:
    if T[-1] == 'A':
        T = T[:len(T)-1]
    elif T[-1] == 'B':
        T = T[:len(T)-1]
        T = T[::-1]
    else:
        result = 0
        break

    if len(T) < len(S):
        result = 0
        break

print(result)