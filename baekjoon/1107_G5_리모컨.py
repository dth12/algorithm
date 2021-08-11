target = int(input())
L = len(str(target))
M = int(input())
if M > 0:
    broken = list(map(int, input().split()))
else:
    broken = []
button = []
answer = 100000000

for i in range(10):
    if i in broken: continue
    button.append(i)

for i in range(1000001):
    num = list(map(int, str(i)))
    possible = 1
    for j in num:
        if j not in button:
            possible = 0
            break

    if possible:
        answer = min(answer, len(num) + abs(i - target))


print(min(answer, abs(target - 100)))






