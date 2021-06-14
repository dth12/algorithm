def binary_search(target: int):

    end = len(num) - 1
    start = 0

    while start <= end:

        mid = (start + end)//2

        if num[mid] == target:
            return 1
        elif num[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
num = list(map(int, input().split()))
num.sort()
M = int(input())
find_list = list(map(int, input().split()))

for target in find_list:
    print(binary_search(target))
