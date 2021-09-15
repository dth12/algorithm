T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAX = 0
    boxes = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        boxes[i].sort(reverse=True)

    boxes.sort()
    print(boxes)
    print('#%d %d' % (tc, MAX))
