import sys
sys.stdin = open("input.txt", "r")

def dfs(v, dist):
    global MAX

    MAX = max(MAX, dist)

    for w in adj[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w, dist+1)
            visited[w] = 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    MAX = 1
    temp = [list(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        p = temp[i][0]
        c = temp[i][1]
        adj[p].append(c)
        adj[c].append(p)

    for v in range(1, V+1):
        visited = [0 for _ in range(V + 1)]
        visited[v] = 1
        dfs(v, 1)

    print('#{} {}'.format(tc, MAX))