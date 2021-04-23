import sys
sys.stdin = open("input.txt", "r")

def bf(idx):
    global cnt
    if idx == N:
        cnt += 1
        return

    for i in range(N):
        if not visit_col[i] and not visit_dia_L[idx-i+N-1] and not visit_dia_R[idx+i]:
            visit_col[i] = 1
            visit_dia_L[idx-i+N-1] = 1
            visit_dia_R[idx+i] = 1
            bf(idx+1)
            visit_col[i] = 0
            visit_dia_L[idx-i+N-1] = 0
            visit_dia_R[idx+i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    visit_col = [0 for _ in range(N)]
    visit_dia_L = [0 for _ in range(2*N-1)]
    visit_dia_R = [0 for _ in range(2*N-1)]
    cnt = 0
    bf(0)
    print('#{} {}'.format(tc, cnt))
