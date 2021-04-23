import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(start):
    queue = deque([start])
    dist = -1
    while queue:
        L = len(queue)
        dist += 1
        for i in range(L):
            v = queue.popleft()
            if v == M:
                return dist
            if v + 1 <= 1000000 and not repeat[v+1]:
                queue.append(v+1)
                repeat[v+1] = 1
            if 1 <= v - 1 and not repeat[v-1]:
                queue.append(v-1)
                repeat[v-1] = 1
            if v * 2 <= 1000000 and not repeat[v*2]:
                queue.append(v*2)
                repeat[v*2] = 1
            if 1 <= v - 10 and not repeat[v-10]:
                queue.append(v-10)
                repeat[v-10] = 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    repeat = [0] * 10000001
    answer = bfs(N)


    print('#{} {}'.format(tc, answer))

