def solution(msg):
    
    L = len(msg)
    msg += '^'
    dict_ = {}
    for i in range(65, 91):
        val = 1 + i % 65
        dict_[chr(i)] = val  
    
    last = 27
    w = ''
    answer = []
    for i in range(L):
        w += msg[i]
        c = msg[i+1]
        temp = w + c
        if temp not in dict_:
            answer.append(dict_[w])
            dict_[temp] = last
            last += 1
            w = ''
            
    print(answer)
    return answer