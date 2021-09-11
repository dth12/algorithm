def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    cache = []

    cur = k
    for c in cmd:
        if c[0] == 'U':
            num = int(c[2:])
            for _ in range(num):
                cur = linked_list[cur][0]
        elif c[0] == 'D':
            num = int(c[2:])
            for _ in range(num):
                cur = linked_list[cur][1]
        elif c[0] == 'C':
            front = linked_list[cur][0]
            rear = linked_list[cur][1]
            cache.append(cur)
            if front >= 0: linked_list[front][1] = rear
            if rear < n: linked_list[rear][0] = front
            cur = rear if rear < n else front
        elif c[0] == 'Z':
            r = cache.pop()
            front = linked_list[r][0]
            rear = linked_list[r][1]
            if front >= 0: linked_list[front][1] = r
            if rear < n: linked_list[rear][0] = r

    answer = ''
    cache = set(cache)
    for i in range(n):
        if i in cache:
            answer += 'X'
        else:
            answer += 'O'

    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))