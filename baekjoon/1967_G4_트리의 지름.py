import sys
from collections import deque

'''
    내가 생각하지 못한 지점 => 만약 완전히 memo에 자식들의 최대값이 저장되지 않았을 때 갱신함.
'''

input = sys.stdin.readline
N = int(input())
# 이진트리라는 정보가 없기에 리스트에 담습니다.
# tree => 자식의 번호를 담습니다. 1번 2번 인덱스에 차례로 부모 노드의 번호, 가중치를 담습니다.
tree = [[[], 0, 0] for _ in range(N + 1)]
# memo[i]의 0번 인덱스는 i 노드를 중심으로 한 지름의 최대 크기를 담습니다.
# memo[i]의 1번 인덱스는 i 노드의 자식 루트 중 가장 큰 값을 가지고 있습니다.
memo = [[0, []] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[0] = 1

for _ in range(N - 1):
    p, c, cost = map(int, input().split())
    tree[p][0].append(c)
    tree[c][1] = p
    tree[c][2] = cost

# 가장 끝 노드들부터 시작하기 위해서 담습니다.
leaf_nodes = deque([])
for i in range(1, N + 1):
    if tree[i][0] == []:
        leaf_nodes.append(i)

# 리프노드
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



