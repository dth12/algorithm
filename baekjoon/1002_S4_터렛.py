from math import sqrt, pow

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        dist = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        if (dist + r2 < r1) or (dist + r1 < r2) or r1 + r2 < dist:
            print(0)
        elif r1 + r2 - 0.0000000001 <= dist <= r1 + r2 + 0.0000000001:
            print(1)
        elif r2 - 0.0000000001 <= dist + r1 <= r2 + 0.0000000001 or r1 - 0.0000000001 <= dist + r2 <= r1 + 0.0000000001:
            print(1)
        else:
            print(2)