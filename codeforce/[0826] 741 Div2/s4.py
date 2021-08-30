import sys
from itertools import combinations

N, K = map(int, input().split())
points = []
answer = 2000 * 2000

for _ in range(N):
    temp = list(map(int, input().split()))
    points.append(temp)

for p1, p2 in combinations(points, 2):

    visited = [0 for _ in range(K + 1)]

    x1, y1, k1 = p1
    x2, y2, k2 = p2

    left_x = min(x1, x2)
    right_x = max(x1, x2)
    bottom_y = min(y1, y2)
    top_y = max(y1, y2)
    square = (right_x - left_x) * (top_y - bottom_y)

    for x, y, k in points:
        if left_x <= x <= right_x and bottom_y <= y <= top_y:
            visited[k] = 1

    if sum(visited) == K:
        answer = min(square, answer)

print(answer)



