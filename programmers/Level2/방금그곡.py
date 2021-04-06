def solution(m, musicinfos):
    
    answer = []
    mm = ''
    new = ''
    mel = {
        'C#': '1',
        'D#': '2',
        'F#': '3',
        'G#': '4',
        'A#': '5',
        'E#': '6',
    }
    
    idx = 0
    while idx < len(m):
        if idx < len(m) - 1 and m[idx+1] == '#':
            temp = m[idx] + m[idx+1]
            new += mel[temp]
            idx += 2
        else:
            new += m[idx]
            idx += 1
            
    mm = new

    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        idx = 0
        new = ''
        while idx < len(musicinfos[i][3]):
            if idx < len(musicinfos[i][3]) - 1 and musicinfos[i][3][idx+1] == '#':
                temp = musicinfos[i][3][idx] + musicinfos[i][3][idx+1]
                new += mel[temp]
                idx += 2
            else:
                new += musicinfos[i][3][idx]
                idx += 1
        
        musicinfos[i][3] = new
        hour = int(musicinfos[i][1][:2]) - int(musicinfos[i][0][:2])
        minute = int(musicinfos[i][1][3:]) - int(musicinfos[i][0][3:])
        time = hour * 60 + minute
        musicinfos[i] = [time] + musicinfos[i][2:]
    
    for info in musicinfos:
        time = info[0]
        sound = info[2] * (time//len(info[2]))
        sound += info[2][:time % len(info[2])+1]
        
        if mm in sound:
            if answer:
                if answer[0] < info[0]:
                    answer = info
            else:
                answer = info
            
    if answer:
        return answer[1]
    else:
        return '(None)'