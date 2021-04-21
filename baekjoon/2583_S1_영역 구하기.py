"""
연습 문제6.
채점 완료 후 해당 화면을 캡처하여 폴더에 첨부하여 업로드 해주세요!

 - BOJ 2583 영역 구하기
 - 그래프 탐색의 가벼운 응용 버전
"""

from collections import deque

R, C, K = map(int, input().split())
# 왼쪽 아래, 오른쪽 위
rec_pos = [list(map(int, input().split())) for _ in range(K)]
visited = [[0 for _ in range(C)] for _ in range(R)]
starts = []
for pos in rec_pos:
    r1, c1 = pos[1], pos[0]
    r2, c2 = pos[3], pos[2]

    for r in range(r1, r2):
        for c in range(c1, c2):
            visited[r][c] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
answer = []

for row in range(R):
    for col in range(C):
        if visited[row][col]: continue
        Q = deque([[row, col]])
        cnt = 0
        while Q:
            r, c = Q.popleft()
            cnt += 1
            visited[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        Q.append([nr, nc])

        if cnt:
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer)




