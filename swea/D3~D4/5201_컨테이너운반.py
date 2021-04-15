import sys
sys.stdin = open("input.txt", "r")
'''
    1. 순열을 생성한다.
    2. 각 순열에서 생성되는 값을 더해서 total에 넣어준다.
    3. Backtracking 조건으로 MIN보다 total이 커지면 return
    4. 마지막까지 비교 후, MIN보다 작으면 넣어준다.

'''
def perm(idx, total):
    global MIN
    if total > MIN:
        return
    elif idx == N-1:
        MIN = min(total+graph[sel[idx-1]][0], MIN)
    else:
        for i in range(N-1):
            if check[i] == 0:
                sel[idx] = num[i]
                check[i] = 1
                if idx:
                    perm(idx+1, total+graph[sel[idx-1]][sel[idx]])
                else:
                    perm(idx + 1, total + graph[0][sel[idx]])
                check[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    num = list(range(1, N))
    sel = [0] * (N-1)
    check = [0] * (N-1)
    MIN = 10000
    perm(0, 0)
    print('#{} {}'.format(tc, MIN))