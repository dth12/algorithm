import sys
sys.stdin = open("input.txt", "r")

# 딕셔너리에 담고 시작한다?

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
    # x 위치, y 위치, 이동 방향, 보유 에너지 K
    info = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(info)):
        info[i][0] *= 2
        info[i][1] *= 2


    total = 0
    record = [[] for _ in range(N)]
    visited = [0 for _ in range(N)]

    # 같은 row, col => i - j / 2 시간 후 충돌
    # row - col == row - col
    # 담을 것들 : 충돌시간, 인덱스?
    for i in range(N):
        x = info[i][0]
        y = info[i][1]
        dir = info[i][2]
        for j in range(i+1, N):
            x_prime = info[j][0]
            y_prime = info[j][1]
            dir_prime = info[j][2]
            if dir_prime == dir or i == j:
                continue
            '''
            -1000 0 3 5
            1000 0 2 3
            0 1000 1 7
            0 -1000 0 9
            
            '''
            # 위로 올라갈 때,
            if dir == 0:
                if y_prime > y and x_prime == x and dir_prime == 1:
                    time = abs(y - y_prime)//2
                    record[i].append([time, i, j])
                elif x_prime > x and y_prime > y and abs(x-x_prime) == abs(y-y_prime) and dir_prime == 2:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])
                elif x_prime < x and y_prime > y and abs(x-x_prime) == abs(y-y_prime)  and dir_prime == 3:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])

            elif dir == 1:
                if y_prime < y and x_prime == x and dir_prime == 0:
                    time = abs(y - y_prime)//2
                    record[i].append([time, i, j])
                elif x_prime > x and y_prime < y and  abs(x-x_prime) == abs(y-y_prime) and dir_prime == 2:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])
                elif x_prime < x and y_prime < y and  abs(x-x_prime) == abs(y-y_prime) and dir_prime == 3:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])

            elif dir == 2:
                if x_prime < x and y == y_prime and dir_prime == 3:
                    time = abs(x - x_prime)//2
                    record[i].append([time, i, j])
                elif y_prime > y and x_prime < x and abs(x-x_prime) == abs(y-y_prime) and dir_prime == 1:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])
                elif y_prime < y and x_prime < x and abs(x-x_prime) == abs(y-y_prime) and dir_prime == 0:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])

            elif dir == 3:
                if x_prime > x and y == y_prime and dir_prime == 2:
                    time = abs(x - x_prime)//2
                    record[i].append([time, i, j])
                elif y_prime > y and x_prime > x and abs(x-x_prime) == abs(y-y_prime) and dir_prime == 1:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])
                elif y_prime < y and x_prime > x and abs(x-x_prime) == abs(y-y_prime) and dir_prime == 0:
                    time = abs(x - x_prime)
                    record[i].append([time, i, j])

    record = sum(record, [])
    record.sort()

    stack = []
    real_time = 0
    if record:
        real_time = record[0][0]
    for i in range(len(record)):
        if real_time == record[i][0] and visited[record[i][1]] == 0 and visited[record[i][2]] == 0:
                stack.append(record[i])
        else:
            real_time = record[i][0]
            while stack:
                v = stack.pop()
                if visited[v[1]] == 0:
                    total += info[v[1]][3]
                    visited[v[1]] = 1

                if visited[v[2]] == 0:
                    total += info[v[2]][3]
                    visited[v[2]] = 1
            if visited[record[i][1]] == 0 and visited[record[i][2]] == 0:
                stack.append(record[i])

    if stack:
        while stack:
            v = stack.pop()
            if visited[v[1]] == 0:
                total += info[v[1]][3]
                visited[v[1]] = 1

            if visited[v[2]] == 0:
                total += info[v[2]][3]
                visited[v[2]] = 1

    print('#{} {}'.format(tc, total))