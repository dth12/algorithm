'''
    좋은 DP 문제라고 생각합니다.
    1) 처음 접근 방법은 추석트래픽처럼 하려고 했습니다.
    2) 두번째 풀이로는 360000짜리 리스트를 생성해서 문제를 해결하려 했으나,
    모든 log마다 배열을 돌면서 += 1 씩 해주는 방식으로는 실패했습니다.
    3) 그래서 외부 풀이를 참고하며 문제를 해결했습니다.

'''
# 00:00:00 형식의 시간을 second로
def time_to_sec(time):
    sec = 0
    for idx, t in enumerate(time.split(':')):
        sec += int(t) * 60 ** (2 - idx)
    return sec


# 17자리 log를 start와 end로 나눔
def log_to_sec(log):
    start, end = log.split('-')
    start_time = 0
    end_time = 0
    for idx, time in enumerate(start.split(':')):
        start_time += int(time) * 60 ** (2 - idx)

    for idx, time in enumerate(end.split(':')):
        end_time += int(time) * 60 ** (2 - idx)

    return start_time, end_time


# 초를 00:00:00 형식으로 변환
def sec_to_log(sec):
    hour = sec // 3600
    sec = sec % 3600
    minute = sec // 60
    sec = sec % 60
    return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, sec)


def solution(play_time, adv_time, logs):

    # 세는 배열
    count_list = [0] * 360001

    # 로그를 돌면서 start와 끝나는 시각을 체크합니다.
    for log in logs:
        start, end = log_to_sec(log)
        count_list[start + 1] += 1
        count_list[end + 1] += -1

    # 각 시간 구간마다 몇개의 동영상이 함께 재생되는지 카운트합니다.
    for i in range(360000):
        count_list[i] += count_list[i - 1]

    # 몇개가 재생되는지 카운트했다면, 각 구간동안 재생된 총시간을 구합니다.
    for i in range(360000):
        count_list[i] += count_list[i - 1]

    adv_sec = time_to_sec(adv_time)

    max_value = count_list[adv_sec] - count_list[0]
    max_start = 0
    for start in range(360000 - adv_sec):
        now = count_list[adv_sec + start] - count_list[start]
        if now > max_value:
            max_value = now
            max_start = start
    return sec_to_log(max_start)