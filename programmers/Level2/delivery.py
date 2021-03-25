# DFS로 풀이
def solution(N, road, K):
    
    answer = 0
    graph = [[10001 for _ in range(N+1)] for _ in range(N+1)] 
    visited = [0] * (N+1)
    memo = [500001] * (N+1)
    
    # 2가지 이상 갈래 있을 경우 작은 것만 저장합니다.
    for i in road:
        if graph[i[0]][i[1]] >= i[2]:
            graph[i[0]][i[1]] = i[2]
            graph[i[1]][i[0]] = i[2]
    
    # DFS로 모든 경로를 파악합니다.
    def dfs(v, distance):
        
        # 만일 거리가 K보다 커진다면 바로 리턴합니다.
        if distance > K:
            return
        
        # 현재 위치보다 더 작은 값이 들어오게 되면 지정해줍니다.
        if memo[v] > distance:
            memo[v] = distance
        # 더 크면 바로 리턴합니다.
        else:
            return
        
        # 방문 처리를 해줍니다.
        visited[v] = 1 
        for i in range(1, N+1):
            if graph[v][i] < 10001 and visited[i] == 0:
                dfs(i, distance + graph[v][i])
                visited[i] = 0
    
    dfs(1, 0)

    for i in range(1, N+1):
        if memo[i] != 500001:
            answer += 1
    
    return answer