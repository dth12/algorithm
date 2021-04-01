def solution(cacheSize, cities):
    answer = 0
    cache = []
    for name in cities:
        city = name.lower()
        
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            answer += 5
            
        cache.append(city)
        if len(cache) == cacheSize + 1:
            cache.pop(0)
    
    return answer