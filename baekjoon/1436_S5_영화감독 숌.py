N = int(input())

cnt = 0
for i in range(666, 10000000):
    str_n = str(i)
    repeat = 0
    for j in range(0, len(str_n)):
        if repeat == 0 and str_n[j] == '6':
            repeat += 1
        elif repeat > 0 and str_n[j] == '6':
            repeat += 1
        elif repeat > 0 and str_n[j] != '6':
            repeat = 0

        if repeat >= 3:
            cnt += 1
            break

    if cnt == N:
        print(i)
        break
