import sys
sys.stdin = open("input.txt", "r")


def partition(start, end):
    pivot = nums[start]
    left = start+1
    right = end
    while left <= right:

        if nums[left] <= pivot:
            left += 1

        if nums[right] > pivot:
            right -= 1

        if left < right and nums[right] <= pivot and nums[left] > pivot:
            nums[left], nums[right] = nums[right], nums[left]

    nums[start], nums[right] = nums[right], nums[start]
    return right


def quick_sort(start, end):
    if start < end:
        pivot = partition(start, end)
        quick_sort(start, pivot-1)
        quick_sort(pivot+1, end)


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, len(nums)-1)
    print('#{} {}'.format(tc, nums[len(nums)//2]))