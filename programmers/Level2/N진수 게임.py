# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 순서p
def solution(n, t, m, p):
    MAX = t*m
    seq = '0'
    answer = ''
    over = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    num = 1
    while len(seq) < MAX:
        N = num
        temp = ''
        while N:
            if N % n >= 10:
                temp = over[N%n] + temp
            else:
                temp = str(N%n) + temp
            N //= n
        seq += temp
        num += 1
    
    for i in range(p, p+t*m, m):
        answer += seq[i-1]
        
    return answer