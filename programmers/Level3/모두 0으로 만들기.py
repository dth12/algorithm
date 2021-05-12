import sys
sys.setrecursionlimit(300000)
def dfs(v: int, a: list, visited: list, tree: list):
    global answer
    
    for w in tree[v]:
        if not visited[w]:
            visited[w] = 1
            a[v] += dfs(w, a, visited, tree)
    
    if v != 0:
        answer += abs(a[v])
    return a[v]
    

def solution(a, edges):
    global answer
    if sum(a) != 0:
        return -1
    
    answer = 0
    # 0: parent, 1: child
    tree = [[] for _ in range(len(a))]
    for v, w in edges:
        tree[w].append(v)
        tree[v].append(w)
    
    visited = [0] * len(a)
    visited[0] = 1
    dfs(0, a, visited, tree)
        
    return answer