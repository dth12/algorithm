def solution(lines):
    times = []
    for line in lines:
        temp = line.split()
        now = temp[1].split(':')  # 현재 시간
        second = now.pop().split('.')
        second[1] = int(second[1]) / 1000
        now += second

        now[0] = int(now[0]) * 3600000
        now[0] += (int(now[1]) * 60000 + int(now[2]) * 1000 + now[3] * 1000)
        time = temp[2][:len(temp[2]) - 1]  # 처리 시간
        if int(now[0]) == 0:
            times.append([0, 0])
            continue
        start_time = now[0] - int(float(time)*1000) + 1
        if start_time < 0:
            start_time = 0
        end_time = now[0]
        if end_time >= 24 * 3600000:
            end_time = 24 * 3600000

        times.append([start_time, max(end_time, 0)])

    
    answer = 0
    for t in times:
        start_cnt = 0
        end_cnt = 0
        for time in times:
            if t[0] <= time[0] < t[0] + 1000 or t[0] <= time[1] < t[0] + 1000 or time[0] <= t[0] < time[1]:
                start_cnt += 1
            if t[1] <= time[0] < t[1] + 1000 or t[1] <= time[1] < t[1] + 1000 or time[0] <= t[1] < time[1]:
                end_cnt += 1
        answer = max(end_cnt, start_cnt, answer)

    return answer