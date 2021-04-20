def powerset(idx):
    global answer

    if sum(check) == M:
        total = 0
        for house in houses:
            MIN = 1000
            for i in range(len(stores)):
                if not check[i]: continue
                r = house[0]
                c = house[1]
                sr = stores[i][0]
                sc = stores[i][1]
                temp = abs(r-sr) + abs(c- sc)
                MIN = min(temp, MIN)
            total += MIN
        answer = min(total, answer)
        return

    if idx == len(stores):
        return

    check[idx] = 0
    powerset(idx+1)
    check[idx] = 1
    powerset(idx+1)


N, M = map(int, input().split())
city = [list(map(int ,input().split())) for _ in range(N)]
houses = []
stores = []
answer = 1000000

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            stores.append([r, c])

check = [0] * len(stores)
powerset(0)
print(answer)