import sys
sys.stdin = open("input.txt", "r")


def find(x):
    temp = x
    while group[x] != x:
        x = group[x]
    group[temp] = x
    return x

def union(x, y):
    root_1 = find(x)
    root_2 = find(y)
    if root_1 != root_2:
        group[root_1] = root_2


for tc in range(1, int(input())+1):
    num_of_people, num_of_relations = map(int, input().split())
    group = list(range(0, num_of_people+1))
    answer = 0

    for _ in range(num_of_relations):
        x, y = map(int, input().split())
        union(x, y)

    for i in range(1, num_of_people+1):
        if group[i] == i:
            answer += 1

    print('#{} {}'.format(tc, answer))



