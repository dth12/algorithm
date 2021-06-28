def solve(start:int, mid: int, end: int, cnt: int ):
    if cnt == 1:
        order.append([start, end])
        return
    else:
        solve(start, end, mid, cnt - 1)
        order.append([start, end])
        solve(mid, end, start, cnt - 1)


N = int(input())
cnt = 0
order = []
state = [[], [i for i in range(N, 0, -1)], [], []]
solve(1, 2, 3, N)
print(len(order))
for i in order:
    print(*i)