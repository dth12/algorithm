def solution(genres, plays):
    songs = dict()
    popular = []
    answer = []
    for i in range(len(genres)):
        if genres[i] in songs:
            songs[genres[i]].append((plays[i], i))
        else:
            songs[genres[i]] = [(plays[i], i)]
            
    for key in songs:
        songs[key].sort(key=lambda x: (-x[0], x[1]))
        total = 0
        for play, pk in songs[key]:
            total += play
        popular.append([total, key])
        
    popular.sort(reverse=True)
    
    for times, genre in popular:
        cnt = 0
        
        for song in songs[genre]:
            if cnt == 2: break
            answer.append(song[1])
            cnt += 1
        
    return answer