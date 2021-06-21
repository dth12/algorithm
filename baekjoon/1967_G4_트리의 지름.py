from collections import deque

N = int(input())
# 자식, 부모 순
tree = [[[], 0, 0] for _ in range(N + 1)]
memo = [[0, []] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[0] = 1

for _ in range(N - 1):
    p, c, cost = map(int, input().split())
    tree[p][0].append(c)
    tree[c][1] = p
    tree[c][2] = cost

leaf_nodes = deque([])
for i in range(1, N + 1):
    if tree[i][0] == []:
        leaf_nodes.append(i)

while leaf_nodes:
    L = len(leaf_nodes)
    for _ in range(L):
        v = leaf_nodes.popleft()
        if visited[v]: continue

        visited[v] = 1
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
        leaf_nodes.append(p)

print(memo)
print(max(memo)[0])



