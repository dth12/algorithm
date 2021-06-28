K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]

answer = 0
start = 1
end = max(wires)

while start <= end:
    mid = (start + end)//2

    cnt = 0
    for wire in wires:
        cnt += wire // mid

    if cnt >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

