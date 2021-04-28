from heapq import heappush, heappop
INF = 2000001
def dijk(V: int, start: int, adj: list) -> list:
    heap = []
    visited = [0] * (V+1)
    dist = [INF] * (V+1) 
    heappush(heap, (0, start))
    
    while heap:
        cost, v = heappop(heap)

        if visited[v]: continue
            
        visited[v] = 1
        dist[v] = cost
        for move_cost, w in adj[v]:
            if not visited[w] and dist[w] > move_cost + cost:
                heappush(heap, (move_cost + cost, w))
        
    return dist
    
    
def solution(V: int, start:int, end_a: int, end_b: int, fares: list) -> int:
    
    adj = [[] for _ in range(V+1)]
    
    for v1, v2, cost in fares:
        adj[v1].append((cost, v2))
        adj[v2].append((cost, v1))
    
    A_to_others = dijk(V, end_a, adj)
    B_to_others = dijk(V, end_b, adj)
    start_to_others = dijk(V, start, adj)
    
    MIN = INF
    for i in range(1, V+1):
        temp = A_to_others[i] + B_to_others[i] + start_to_others[i]
        MIN = min(temp, MIN)
    
    return MIN