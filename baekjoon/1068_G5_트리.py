def remove_from_tree(parent: int) -> None:
    removed.append(parent)
    for child in tree[parent][1]:
        remove_from_tree(child)


N = int(input())
arr = list(map(int, input().split()))
remove = int(input())

tree = [[-1, []] for _ in range(N)]
removed = []

for i in range(N):
    if arr[i] >= 0:
        tree[i][0] = arr[i]
        tree[arr[i]][1].append(i)

remove_from_tree(remove)
cnt = 0
for p in range(N):
    if p in removed: continue
    if tree[p][1]:
        temp = 0
        for c in tree[p][1]:
            if c in removed:
                temp += 1

        if temp == len(tree[p][1]):
            cnt += 1
    else:
        cnt += 1

print(cnt)




