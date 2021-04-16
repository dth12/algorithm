def solution(routes):
    routes.sort()
    MIN = routes[0][0]
    MAX = routes[0][1]
    cnt = 1
    for route in routes:
        start = route[0]
        end = route[1]
        if not (MIN <= start <= MAX or MIN <= end <= MAX):
            MIN = route[0]
            MAX = route[1]
            cnt += 1
        else:
            MIN = max(start, MIN)
            MAX = min(end, MAX)
        
    return cnt