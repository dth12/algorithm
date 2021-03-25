import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    '''
        1 => 오른쪽 위 [0, 1] <=> [-1, 0]
        2 => 아래 오른쪽 [1, 0] <=> [0, 1]
        3 => 왼쪽 아래 [0, -1] <=> [1, 0]
        4 => 위쪽 왼쪽 [-1, 0] <=> [0, -1]
    '''
    N = int(input())
    MAX = 0
    wormhole = {6: [], 7: [], 8: [], 9: [], 10: []}
    board = [list(map(int ,input().split())) for _ in range(N)]
    for r in range(len(board)):
        for c in range(len(board)):
            if 6 <= board[r][c] <= 10:
                wormhole[board[r][c]].append([r, c])
    # 좌 우 상 하
    dir = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1],
    }
    
    change_dir = {
        'U': ['D', 'D', 'R', 'L', 'D', 'D'],
        'D': ['U', 'R', 'U', 'U', 'L', 'U'],
        'L': ['R', 'U', 'D', 'R', 'R', 'R'],
        'R': ['L', 'L', 'L', 'D', 'U', 'L'],
    }

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                for key in dir:
                    ball_dir = key
                    score = 0
                    done = 0
                    if 0 <= r + dir[ball_dir][0] < N and 0 <= c + dir[ball_dir][1] < N:
                        nr = r + dir[ball_dir][0]
                        nc = c + dir[ball_dir][1]
                        while True:
                            if (0 > nr or N <= nr) or (0 > nc or N <= nc):
                                score += 1
                                ball_dir = change_dir[ball_dir][0]
                                nr += dir[ball_dir][0]
                                nc += dir[ball_dir][1]

                            elif board[nr][nc] == -1 or (nr == r and nc == c):
                                done = 1
                                break

                            elif board[nr][nc] == 0:
                                nr += dir[ball_dir][0]
                                nc += dir[ball_dir][1]

                            elif 6 <= board[nr][nc] <= 10:
                                for hole in wormhole[board[nr][nc]]:
                                    if hole[0] != nr or hole[1] != nc:
                                        nr = hole[0] + dir[ball_dir][0]
                                        nc = hole[1] + dir[ball_dir][1]
                                        break

                            elif 1 <= board[nr][nc] <= 5:
                                score += 1
                                ball_dir = change_dir[ball_dir][board[nr][nc]]
                                nr += dir[ball_dir][0]
                                nc += dir[ball_dir][1]

                        if done == 1:
                            MAX = max(MAX, score)
    print('#{} {}'.format(tc, MAX))











