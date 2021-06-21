def find(a: int):
    if arr[a] == a:
        return a
    else:
        arr[a] = find(arr[a])
        return arr[a]


def union(a: int, b: int):
    root_a = find(a)
    root_b = find(b)
    arr[root_a] = root_b


N = int(input())
arr = [i for i in range(N)]
x_positions = []
y_positions = []
z_positions = []
for i in range(N):
    x, y, z = map(int, input().split())
    x_positions.append([x, i])
    y_positions.append([y, i])
    z_positions.append([z, i])

x_positions.sort()
y_positions.sort()
z_positions.sort()

cases = []
for i in range(N - 1):
    x = abs(x_positions[i][0] - x_positions[i + 1][0])
    y = abs(y_positions[i][0] - y_positions[i + 1][0])
    z = abs(z_positions[i][0] - z_positions[i + 1][0])
    cases.append([x, x_positions[i][1], x_positions[i + 1][1]])
    cases.append([y, y_positions[i][1], y_positions[i + 1][1]])
    cases.append([z, z_positions[i][1], z_positions[i + 1][1]])


cases.sort()
answer = 0
cnt = 0
for cost, x, y in cases:
    if cnt == N - 1:
        break

    if find(x) == find(y):
        continue
    else:
        union(x, y)
        answer += cost
        cnt += 1

print(answer)





