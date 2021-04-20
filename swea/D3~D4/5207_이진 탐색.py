import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for target in B:
        left = 0
        right = len(A) - 1
        center = (left + right)//2
        num = A[center]
        flag = -1
        if num == target:
            cnt += 1
            continue

        while left < right and target != num:
            if target > num:
                if flag == 0:
                    break
                left = center + 1
                center = (left+right)//2
                num = A[center]
                flag = 0
            elif target < num:
                if flag == 1:
                    break
                right = center - 1
                center = (left+right)//2
                num = A[center]
                flag = 1

        if target == num and left <= right:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
