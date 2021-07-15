import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    blank = input()
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    if x1 == x2 == x3:
        if y1 > y2 and y2 <= y3 <= y1:
            print(y1 - y2 + 2)
        elif y1 < y2 and y1 <= y3 <= y2:
            print(y2 - y1 + 2)
        else:
            print(abs(y1 - y2))
    elif y1 == y2 == y3:
        if x1 > x2 and x2 <= x3 <= x1:
            print(x1 - x2 + 2)
        elif x1 < x2 and x1 <= x3 <= x2:
            print(x2 - x1 + 2)
        else:
            print(abs(x1 - x2))
    else:
        print(abs(x1 - x2) + abs(y1 - y2))
