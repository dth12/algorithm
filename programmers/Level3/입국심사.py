def solution(n, times):
    MIN = min(times)
    end = MIN * n
    start = 0
    answer = 0
    while start <= end:
        center1 = (end + start) // 2
        center2 = center1 - 1

        total1, total2 = 0, 0
        for time in times:
            total1 += center1 // time
            total2 += center2 // time

        if total1 >= n and total2 < n:
            answer = center1
            break
        elif total1 < n and total2 < n:
            start = center1 + 1
        elif total1 >= n and total2 >= n:
            end = center1 - 1

    return answer