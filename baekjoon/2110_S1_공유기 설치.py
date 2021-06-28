N, C = map(int, input().split())
x_pos = [int(input()) for _ in range(N)]
x_pos.sort()

start = 1
answer = 0
end = x_pos[-1] - x_pos[0]

while start <= end:
    mid = (start + end)//2

    cnt = [x_pos[0]]
    for i in range(1, len(x_pos)):
        if x_pos[i] - cnt[-1] >= mid:
            cnt.append(x_pos[i])

    if len(cnt) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

