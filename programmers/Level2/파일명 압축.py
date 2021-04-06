def solution(files):
    copy = [0 for _ in range(len(files))]
    special = [' ', '.', '-']
    for i in range(len(files)):
        head = ''
        tail = ''
        idx = 0
        while (files[i][idx].isalpha() or files[i][idx] in special) :
            head += files[i][idx]
            idx += 1

        while idx < len(files[i]) and files[i][idx].isdecimal():
            tail += files[i][idx]
            idx += 1
        
        copy[i] = [head.lower(), int(tail)]
    
    
    for i in range(len(files)-1, 0, -1):
        for j in range(i):
            if copy[j][0] > copy[j+1][0]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
                files[j], files[j+1] = files[j+1], files[j]
            elif copy[j][0] == copy[j+1][0]:
                if copy[j][1] > copy[j+1][1]:
                    copy[j], copy[j+1] = copy[j+1], copy[j]
                    files[j], files[j+1] = files[j+1], files[j]
                
    return files