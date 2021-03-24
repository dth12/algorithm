import sys
sys.stdin = open("input.txt", "r")

#1 1200
#2 3290
#3 16620
#4 40650
#5 52710

T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split())

    # 0 1 2 3 4
    # X U R D L
    move = {0:[0, 0], 1: [0, -1], 2: [1, 0], 3: [0, 1], 4: [-1, 0]}
    pos_A = [0, 0]
    pos_B = [9, 9]
    path_A = list(map(int, input().split())) + [0]
    path_B = list(map(int, input().split())) + [0]
    answer = 0
    # AP => (r, c, 충전거리, 파워)
    AP_info = [list(map(int, input().split())) for _ in range(A)]
    for i in range(len(AP_info)):
        AP_info[i][0] -= 1
        AP_info[i][1] -= 1

    for time in range(M+1):

        temp_charged = 0
        possible_AP = {'A': [], 'B': []}
        for i in range(len(AP_info)):
            r = AP_info[i][0]
            c = AP_info[i][1]
            dist = AP_info[i][2]

            if abs(pos_A[0] - r) + abs(pos_A[1] - c) <= dist:
                possible_AP['A'].append(i)

            if abs(pos_B[0] - r) + abs(pos_B[1] - c) <= dist:
                possible_AP['B'].append(i)

        if possible_AP['A'] and possible_AP['B']:
            for a in possible_AP['A']:
                for b in possible_AP['B']:
                    if a != b:
                        temp_charged = max(AP_info[a][3] + AP_info[b][3], temp_charged)
                    elif a == b:
                        temp_charged = max(AP_info[a][3], temp_charged)
        elif possible_AP['A'] and possible_AP['B'] == []:
            for a in possible_AP['A']:
                temp_charged = max(AP_info[a][3], temp_charged)
        elif possible_AP['A'] == [] and possible_AP['B']:
            for b in possible_AP['B']:
                temp_charged = max(AP_info[b][3], temp_charged)


        answer += temp_charged
        pos_A[0] += move[path_A[time]][0]
        pos_A[1] += move[path_A[time]][1]
        pos_B[0] += move[path_B[time]][0]
        pos_B[1] += move[path_B[time]][1]

    print('#{} {}'.format(tc, answer))

