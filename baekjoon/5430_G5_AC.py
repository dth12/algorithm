# R 뒤집기 D 버리기

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    commands = input()
    N = int(input())
    nums = input()
    nums = nums[1:len(nums) - 2]
    if len(nums) == 0:
        Q = deque([])
    elif len(nums) == 1:
        Q = deque([nums])
    else:
        Q = deque(nums.split(','))

    error = 0
    reverse = 0
    for command in commands:
        if command == 'R':
            reverse = 0 if reverse else 1
        elif command == 'D':
            if len(Q):
                if reverse:
                    Q.pop()
                else:
                    Q.popleft()
            else:
                error = 1
                break
    if reverse:
        Q.reverse()

    if error:
        print('error')
    else:
        print('[', end='')
        for i in range(len(Q)):
            if i < len(Q) - 1:
                print(Q[i] + ',', end='')
            else:
                print(Q[i], end='')
        print(']')
