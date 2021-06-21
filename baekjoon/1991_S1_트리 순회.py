def pre(node: str):
    if node != '.':
        print(node, end='')
        pre(tree[node][0])
        pre(tree[node][1])


def inorder(node: str):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def post(node: str):
    if node != '.':
        post(tree[node][0])
        post(tree[node][1])
        print(node, end='')


N = int(input())
tree = {}

for _ in range(N):
    p, left, right = input().split()
    if p in tree:
        tree[p][0] = left
        tree[p][1] = right
    else:
        tree[p] = [left, right, '.']

    if left in tree:
        tree[left][2] = p
    else:
        tree[left] = ['.', '.', p]

    if right in tree:
        tree[right][2] = p
    else:
        tree[right] = ['.', '.', p]

pre('A')
print()
inorder('A')
print()
post('A')

