import sys
sys.stdin = open("input.txt", "r")

# 크루스칼
def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 != root2:
        p[root1] = root2


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = list(range(V+1))
    answer = 0
    cnt = 0
    # [s1, s2, cost]
    edges.sort(key=lambda x: x[2])

    for v1, v2, cost in edges:
        if cnt == V:
            break
        elif find(v1) != find(v2):
            union(v1, v2)
            answer += cost
            cnt += 1

    print('#{} {}'.format(tc, answer))


