import sys

sys.stdin = open('input3.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    answer = 0
    R, C = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(R)]
    MAX = 0
    stack = []
    for r in range(R):
        for c in range(C):
            if MAX == boxes[r][c]:
                stack.append([r, c])
            elif MAX < boxes[r][c]:
                MAX = boxes[r][c]
                stack = []
                stack.append([r, c])

    MAX = MAX + 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while stack:
        MAX -= 1
        temp_stack = []
        for _ in range(len(stack)):
            v = stack.pop()
            r = v[0]
            c = v[1]
            for i in range(4):
                if 0 <= r + dr[i] < R and 0 <= c + dc[i] < C and boxes[r+dr[i]][c+dc[i]] < MAX:
                    temp = answer
                    answer += (MAX - 1 - boxes[r+dr[i]][c+dc[i]])
                    boxes[r+dr[i]][c+dc[i]] = MAX - 1
                    temp_stack.append([r+dr[i], c+dc[i]])
        stack = temp_stack

    print('Case #{}: {}'.format(tc, answer))