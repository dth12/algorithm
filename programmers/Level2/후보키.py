def solution(relation):
    answer = 0
    R = len(relation)
    C = len(relation[0])
    pk = []
    num = []
    field = {}
    
    for i in range(len(relation)):
        for j in range(C):
            if j in field:
                field[j].add(relation[i][j])
            else:
                field[j] = {relation[i][j]}
    
    for key in range(C):
        if len(field[key]) == R: 
            pk.append(j)
        else:
            num.append(key)
    
    answer += len(pk)
    pk = []
    num.sort()
    sel = [0] * len(num)
    
    def powerset(idx):
        nonlocal pk
        
        if idx == len(num):
            ck = []
            for i in range(len(num)):
                if sel[i] == 1:
                    ck.append(num[i])
                
            repeat = set()
            for i in range(R):
                temp = []
                for j in ck:
                    temp.append(relation[i][j])
                repeat.add(tuple(temp))
            
            if len(repeat) == R:
                for key in pk:
                    if set(key).issubset(set(ck)):
                        break
                else:
                    pk.append(ck)
            return
        
        sel[idx] = 0
        powerset(idx+1)
        sel[idx] = 1
        powerset(idx+1)
    
    powerset(0)
    return answer + len(pk)