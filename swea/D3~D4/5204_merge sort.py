import sys
sys.stdin = open("input.txt", "r")


def merge_sort(arr) -> list:
    if len(arr) == 1:
        return arr
    else:
        L = len(arr)
        arr1 = merge_sort(arr[0:L//2])
        arr2 = merge_sort(arr[L//2:L])
        return merge(arr1, arr2)

def merge(arr1: list, arr2: list):
    global cnt

    if arr1[-1] > arr2[-1]:
        cnt += 1

    temp = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] <= arr2[idx2]:
            temp.append(arr1[idx1])
            idx1 += 1
        elif arr1[idx1] > arr2[idx2]:
            temp.append(arr2[idx2])
            idx2 += 1

    if idx1 < len(arr1):
        temp += arr1[idx1:]
    elif idx2 < len(arr2):
        temp += arr2[idx2:]

    return temp


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    answer = merge_sort(nums)
    print('#{} {} {}'.format(tc, answer[N//2], cnt))

