'''
    ex) N = 5
    1. 
        memo[1] = {5}
        
    2. 
        5 - 5
        5 * 5
        5 + 5
        5 // 5
        memo[2] = {0, 1, 10, 25}
        
    3. 
        memo[1]과 memo[2] 계산
        memo[2]와 memo[1] 계산
        
    4. 
        memo[1]와 memo[3] 계산
        memo[3]와 memo[1] 계산
        memo[2]와 memo[2] 계산
        
    ...
'''

def solution(N, number):
    if N == number:
        return 1
    
    memo = [set() for _ in range(9)]
    
    for i in range(1, 9):
        temp = int(i * str(N))
        memo[i].add(temp)
        
        for j in range(1, i):
            for num1 in memo[j]:
                for num2 in memo[i-j]:
                    memo[i].add(num1+num2)
                    memo[i].add(num1*num2)
                    memo[i].add(num1-num2)
                    if num2: memo[i].add(num1//num2)
                        
        if number in memo[i]:
            return i
        
    return -1