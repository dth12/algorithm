N, M = map(int, input().split())
targets = list(map(int, input().split()))
Q = list(range(1, N + 1))

answer = 0
for target in targets:
    if Q[0] == target:
        Q.pop(0)
    elif Q[-1] == target:
        Q.pop()
        answer += 1
    else:
        pos = Q.index(target)
        if pos > len(Q) // 2:
            answer += len(Q) - pos
            Q = Q[pos + 1:] + Q[:pos]
        else:
            answer += pos
            Q = Q[pos + 1:] + Q[:pos]

print(answer)









