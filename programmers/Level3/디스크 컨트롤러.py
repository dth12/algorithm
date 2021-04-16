from heapq import heappop, heappush
def solution(jobs):
    heap = []
    
    jobs.sort()
    # jobs[i] = [처리시간, 요청시간]으로 순서변경. 힙을 사용하기 위해서
    for i in range(len(jobs)):
        jobs[i] = jobs[i][::-1]

    time = jobs[0][1]
    total = 0
    idx = 0
    cnt = 0
    now = []
    while cnt < len(jobs):
        if now:
            while idx < len(jobs) and time - now[0] <= jobs[idx][1] <= time:
                heappush(heap, jobs[idx])
                idx += 1
        if heap:
            now = heappop(heap)
            total += (time + now[0] - now[1])
            time += now[0]
            cnt += 1
        else:
            now = jobs[idx]
            total += (now[0])
            time = now[1] + now[0]
            idx += 1
            cnt += 1

    return int(total / len(jobs))