T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    times = [0] + times
    condition = [[] for _ in range(N + 1)]

    for _ in range(K):
        f, s = map(int, input().split())
        condition[s].append(f)

    target = int(input())
    temp = [target]
    all_built = {target}
    while True:
        cnt = 0
        next_temp = []
        for v in temp:
            for w in condition[v]:
                if w in all_built: continue
                next_temp.append(w)
                all_built.add(w)

        if next_temp:
            temp = next_temp
        else:
            break

    already_built = set()
    time = 0
    record_times = [0 for _ in range(N + 1)]
    while True:
        now = set()
        for v in all_built:
            if v not in already_built:
                flag = True
                for w in condition[v]:
                    if w not in already_built:
                        flag = False
                        break

                if flag:
                    now.add(v)

        if target in now:
            break

        for v in now:
            already_built.add(v)
            temp_time = 0
            for w in condition[v]:
                temp_time = max(record_times[w], temp_time)

            record_times[v] = temp_time + times[v]
            time = max(time, record_times[v])

    print(time + times[target])
    # 실패 이유 :
    # 만약 동시에 짓는 건물을 짓던 중, 하나가 끝나고
    # 다른 하나를 더 지을 수 있는 경우를 생각하지 못함.
    # answer = times[target]
    # while True:
    #     now = set()
    #     for v in all_built:
    #         if v not in already_built:
    #             flag = True
    #             for w in condition[v]:
    #                 if w not in already_built:
    #                     flag = False
    #                     break
    #
    #             if flag:
    #                 now.add(v)
    #
    #     if target in now:
    #         break
    #
    #     max_time = 0
    #     for v in now:
    #         already_built.add(v)
    #         max_time = max(max_time, times[v])
    #
    #     answer += max_time
    #
    # print(answer)




























