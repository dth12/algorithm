import sys
sys.stdin = open("input.txt", "r")

def find(x):
    temp = x
    while p[x] != x:
        x = p[x]

    p[temp] = x
    return x


def union(x, y):
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        p[root1] = root2


num_of_cities = int(input())
num_of_plan = int(input())

p = list(range(num_of_cities))
adj = [list(map(int, input().split())) for _ in range(num_of_cities)]
plan = list(map(int, input().split()))

for to_ in range(num_of_cities):
    for from_ in range(num_of_cities):
        if adj[to_][from_]:
            union(to_, from_)

root = find(plan[0]-1)
answer = 'YES'
for i in range(1, len(plan)):
    if find(plan[i]-1) != root:
        answer = 'NO'
        break

print(answer)

