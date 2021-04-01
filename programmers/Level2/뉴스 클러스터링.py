def solution(str1, str2):
    if len(str1) > len(str2):
        str2, str1 = str1, str2
    
    dict_str1 = {}
    dict_str2 = {}
    stack = ''
    for char in str1:
        if char.isalpha():
            stack += char.lower()
        else:
            stack = ''
            
        if len(stack) == 2:
            if stack in dict_str1:
                dict_str1[stack] += 1
            else:
                dict_str1[stack] = 1
            stack = stack[1]
    
    stack = ''
    for char in str2:        
        if char.isalpha():
            stack += char.lower()
        else:
            stack = ''
        
        if len(stack) == 2:
            if stack in dict_str2:
                dict_str2[stack] += 1
            else:
                dict_str2[stack] = 1
            stack = stack[1]
    
    union = 0
    inter = 0
    for key in dict_str1:
        if key in dict_str2:
            inter += min(dict_str1[key], dict_str2[key])
        else:
            union += dict_str1[key]

    for key in dict_str2:
        if key in dict_str1:
            union += max(dict_str1[key], dict_str2[key])
        else:
            union += dict_str2[key]
    
    if union != 0:
        answer = int(inter/union*65536)
    else:
        answer = 65536
    return answer