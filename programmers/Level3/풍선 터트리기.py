# 하나만 빼고 전부 다 터트렸을 때,
# 양 사이드는 무조건 살아남음.
def solution(a):
    if len(a) <= 3:
        return len(a)
    
    answer = 2
    aa = [[0 for _ in range(2)] for _ in range(len(a))]
    R = a[0]
    L = a[-1]
    
    for idx in range(1, len(a)-1):
        aa[idx][0] = R
        aa[len(a)-idx-1][1] = L

        if R > a[idx]:
            R = a[idx]
        
        if L > a[len(a)-idx-1]:
            L = a[len(a)-idx-1]
    
    
    for idx in range(1, len(a)-1):
        R = aa[idx][0]
        L = aa[idx][1]
        
        if R > a[idx] or L > a[idx]:
            answer += 1
            
    return answer