def dfs(stack, visited, computers):
    while stack:
        v = stack.pop()
        visited[v] = 1
        computer = computers[v]
        for i in range(len(computer)):
            if computer[i] and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
        
def solution(n, computers):
    # computers => 인접 행렬
    stack = []
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            stack = [i]
            dfs(stack, visited, computers)
            answer += 1
    
    return answer