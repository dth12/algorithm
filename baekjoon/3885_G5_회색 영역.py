while True:
    n, m = map(int, input().split())
    if n == 10:
        debug = True
    if n and m:
        nums = [int(input()) for _ in range(n)]
        max_val = max(nums)
        intervals = [(i - m, i) for i in range(m, max_val + m + 1, m)]
        count_list = [0 for _ in range(len(intervals))]
        for num in nums:

            for i in range(len(intervals)):
                if intervals[i][0] <= num < intervals[i][1]:
                    count_list[i] += 1
                    break

        max_cnt = max(count_list)
        L = len(count_list) - 1
        answer = 0
        brightness = 1
        for i in count_list:
            answer += (i / max_cnt) * brightness
            brightness -= 1 / L

        print(answer + 0.01)
    else:
        break