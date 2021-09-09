def solution(a, b, g, s, w, t):
    times = []
    for idx, time in enumerate(t):
        times.append((time * 2, idx))

    times.sort()
    answer = 0
    start = 0
    end = 2000000001

    while start <= end:
        mid = (start + end) // 2

        total_gold = 0
        total_silver = 0
        total_limit_weight = 0
        for time, i in times:
            repeat = mid // time
            if mid % time >= time // 2:
                repeat += 1
            limit_weight = repeat * w[i]
            total_limit_weight += limit_weight
            total_gold += min(limit_weight, g[i])
            total_silver += min(limit_weight, s[i])

        if total_gold > a and total_silver > b and a + b < total_limit_weight:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
