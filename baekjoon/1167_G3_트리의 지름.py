import sys
from collections import deque
input = sys.stdin.readline
def dfs(node: int, total: int):
    global MAX, end

    if MAX < total:
        end = node
        MAX = total

    for cost, next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, total + cost)


N = int(input())
MAX = 0
end = 0

temp_tree = [[] for _ in range(N + 1)]
tree = [[[], 0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
memo = [[0, []] for _ in range(N + 1)]

for _ in range(N - 1):
    temp = list(map(int, input().split()))
    v = temp[0]
    for i in range(1, len(temp) - 1, 2):
        temp_tree[v].append([temp[i + 1], temp[i]])  # 가중치, 정점
        temp_tree[temp[i]].append([temp[i + 1], v])


Q = deque([1])
visited[1] = 1
while Q:
    v = Q.popleft()
    for cost, w in temp_tree[v]:
        if not visited[w]:
            visited[w] = 1
            tree[v][0].append(w)
            tree[w][1] = v
            tree[w][2] = cost
            Q.append(w)

leaf_nodes = deque([])
for i in range(1, N + 1):
    if tree[i][0] == []:
        leaf_nodes.append(i)

while leaf_nodes:
    L = len(leaf_nodes)
    for _ in range(L):
        v = leaf_nodes.popleft()
        if v == 0:
            break

        p = tree[v][1]
        max_route = 0
        if len(memo[v][1]) > 2:
            memo[v][1].sort()
            memo[v][0] = memo[v][1][-1] + memo[v][1][-2]
        else:
            memo[v][0] = sum(memo[v][1])

        max_value = max(memo[v][1]) if memo[v][1] else 0
        max_value += tree[v][2]
        memo[p][1].append(max_value)

        if len(memo[p][1]) == len(tree[p][0]):
            leaf_nodes.append(p)

print(max(memo)[0])





