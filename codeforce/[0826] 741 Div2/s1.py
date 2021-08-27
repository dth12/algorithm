T = int(input())

for tc in range(T):
    l, r = map(int, input().split())
    if l == r:
        print(0)
    else:
        q = max(l, r // 2 + 1)
        print(r % q)