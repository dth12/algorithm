import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * N)

answer = 0
cnt = 0

while cnt < K:
    answer += 1

    # 1번
    belt.appendleft(belt.pop())
    robots.pop()
    robots.appendleft(0)

    # 2번
    robots[N-1] = 0
    for i in range(N-2, -1, -1):
        if belt[i+1] > 0 and robots[i] == 1 and robots[i+1] == 0:
            robots[i], robots[i+1] = robots[i+1], robots[i]
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1

    # 3번
    if belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

print(answer)




