from collections import deque


def find_leaf(node: int) -> None:
    if node in leaf:
        start.add(node)
        return
    else:
        for v in order[node][0]:
            find_leaf(v)
            all_node.add(v)


def is_next(node: int) -> bool:

    for v in order[node][0]:
        if v not in visited:
            return False

    return True

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    order = [[set(), set()] for _ in range(N)]
    leaf = set()

    for _ in range(K):
        f, s = map(int, input().split())
        order[s - 1][0].add(f - 1)
        order[f - 1][1].add(s - 1)

    last = int(input()) - 1

    for v in range(N):
        if len(order[v][0]) == 0:
            leaf.add(v)

    if last in leaf:
        print(times[last])
    else:
        if _ == 2:
            debug = True
        start = set()
        all_node = {last}
        find_leaf(last)
        answer = times[last]
        next_nodes = {i for i in start}
        visited = {i for i in start}

        if times[0] == 100000:
            debug = True

        while True:
            temp = set()
            stay = set()
            lazy_visited = set()
            max_time = 0
            for v in next_nodes:
                if not is_next(v):
                    stay.add(v)
                    continue
                max_time = max(times[v], max_time)
                lazy_visited.add(v)
                for w in order[v][1]:
                    if w in all_node:
                        temp.add(w)

            for v in lazy_visited:
                visited.add(v)

            if last in visited:
                print(answer)
                break

            next_nodes = {i for i in temp.union(stay)}
            answer += max_time






















