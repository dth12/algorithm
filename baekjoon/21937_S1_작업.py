import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int, input().split())
rel = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    rel[end].append(start)

target = int(input())
visited[target] = 1
queue = deque([target])
cnt = 0
while queue:
    v = queue.popleft()

    for w in rel[v]:
        if not visited[w]:
            cnt += 1
            visited[w] = 1
            queue.append(w)

print(cnt)

