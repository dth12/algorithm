N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: (x[0], x[1]))

cnt = 0
for i in range(N):
    x1, y1 = points[i]
    memo = [set(), set()]
    for j in range(i + 1, N):
        x2, y2 = points[j]
        x = x2 - x1
        y = y2 - y1

        if x == 0 and y > 0:
            memo[1].add(y)
        elif x > 0 and y == 0:
            memo[0].add(x)
        else:
            if x in memo[0] and y in memo[1]:
                cnt += 1

print(cnt)


