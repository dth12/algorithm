def solution(n, costs):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    MIN = 100000000000000000000
    # [섬1, 섬2, cost]
    for info in costs:
        isl_1 = info[0]
        isl_2 = info[1]
        cost = info[2]
        graph[isl_1][isl_2] = cost
        graph[isl_2][isl_1] = cost

    for i in range(n):
        visited = [0 for _ in range(n)]
        stack = [i]
        visited[i] = 1
        total_cost = 0
        while stack:
            v = stack.pop()
            temp = 10000000000
            min_cost_isl = -1
            for w in range(n):
                if visited[w] == 0 and graph[v][w]:
                    if graph[v][w] < temp:
                        temp = graph[v][w]
                        min_cost_isl = w

            if min_cost_isl != -1:
                visited[min_cost_isl] = 1
                stack.append(min_cost_isl)
                total_cost += graph[v][min_cost_isl]

        MIN = min(MIN, total_cost)

    return MIN

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
