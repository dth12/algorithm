"""
연습 문제5.
채점 완료 후 해당 화면을 캡처하여 폴더에 첨부하여 업로드 해주세요!

 - BOJ 2606 바이러스
 - 기본적인 그래프 탐색 문제
"""
import sys
sys.stdin = open('input.txt')

def dfs(v):
    global cnt

    cnt += 1
    for w in adj[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)

V = int(input())
E = int(input())

cnt = 0
adj = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(E):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)

visited[1] = 1
dfs(1)
print(cnt-1)



