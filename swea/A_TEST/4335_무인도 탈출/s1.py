import sys
sys.stdin = open("input.txt", "r")

def perm(idx, total, path):
    global MAX

    MAX = max(total, MAX)



    if idx == N:
        return
    else:
        for i in range(N):
            if not check[i]:
                for j in range(3):
                    w, d, h = boxes[i][j]
                    if idx == 0:
                        sel[idx][0] = i
                        sel[idx][1] = j
                        check[i] = 1
                        perm(idx + 1, total + h)
                        check[i] = 0
                    else:
                        ww, dd, hh = boxes[sel[idx-1][0]][sel[idx-1][1]]
                        if (w <= ww and d <= dd) or (w <= dd and d <= ww):
                            sel[idx][0] = i
                            sel[idx][1] = j
                            check[i] = 1
                            perm(idx + 1, total + h)
                            check[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxes_origin = [list(map(int, input().split())) for _ in range(N)]
    boxes = [0] * N
    for k in range(N):
        a, b, c = boxes_origin[k]
        boxes[k] = [[a, b, c], [b, c, a], [a, c, b]]

    sel = [[0, 0] for _ in range(N)]
    check = [0] * N
    MAX = 0
    perm(0, 0)
    print('#%d %d' % (tc, MAX))
