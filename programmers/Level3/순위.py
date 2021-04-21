def solution(n, results):
    answer = 0
    # 나에게 진 사람들
    winner = {key:set() for key in range(1, n+1)}
    # 내가 진 사람들
    loser = {key:set() for key in range(1, n+1)}
    for result in results:
        win, de = result
        winner[win].add(de)
        loser[de].add(win)
    
    for p1 in range(1, n+1):
        # 나를 이긴 사람은 나에게 진 사람을 이깁니다.
        for win in loser[p1]:
            for defeat in winner[p1]:
                winner[win].add(defeat)
        
        # 나에게 진 사람은 나에게 이긴 사람에게 집니다.
        for defeat in winner[p1]:
            for win in loser[p1]:
                loser[defeat].add(win)
    
    # 나를 이긴 사람과 나에게 이긴 사람의 수가 같으면 카운트를 올려줍니다.
    for player in range(1, n+1):
        if len(winner[player]) + len(loser[player]) == n-1:
            answer += 1
                
    return answer