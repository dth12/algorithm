answer = 9


def inrange(distance: int, cur_pos: int, target: int, n: int, clockwise: bool) -> bool:
    if clockwise:
        diff = target - cur_pos
    else:
        diff = cur_pos - target

    if 0 <= diff <= distance:
        return True
    elif diff < 0:
        diff += n
        if diff <= distance:
            return True
        else:
            return False
        
    return False


def dfs(n: int, idx: int, weaks: list, dist: list, visited: list) -> None:
    global answer

    if idx >= answer or idx >= len(dist):
        return

    flag = 0
    for i in range(len(weaks)):
        if visited[i] == 0:
            flag = 1
            break

    if flag == 0:
        answer = min(answer, idx)
        return

    for i in range(len(weaks)):
        new_left_visited = [ele for ele in visited]
        new_right_visited = [ele for ele in visited]

        for j in range(len(weaks)):  # 시계 방향
            if inrange(dist[idx], weaks[i], weaks[j], n, True):
                new_left_visited[j] = 1

            if inrange(dist[idx], weaks[i], weaks[j], n, False):
                new_right_visited[j] = 1

        dfs(n, idx + 1, weaks, dist, new_left_visited)
        dfs(n, idx + 1, weaks, dist, new_right_visited)


def solution(n, weaks, dist) -> int:
    global answer
    dist = dist[::-1]
    visited = [0 for _ in range(len(weaks))]

    dfs(n, 0, weaks, dist, visited)

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))