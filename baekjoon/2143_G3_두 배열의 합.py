def combination(nums: list) -> dict:
    comb = dict()
    for i in range(len(nums)):
        if nums[i] in comb:
            comb[nums[i]] += 1
        else:
            comb[nums[i]] = 1
        for j in range(i):
            if nums[i] - nums[j] in comb:
                comb[nums[i] - nums[j]] += 1
            else:
                comb[nums[i] - nums[j]] = 1

    return comb


def find(nums: list, num: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if num + nums[mid] == T:
            return comb_A[nums[mid]]
        elif num + nums[mid] > T:
            end = mid - 1
        else:
            start = mid + 1

    return 0


T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(1, N):
    A[i] += A[i - 1]

for i in range(1, M):
    B[i] += B[i - 1]

answer = 0
comb_A = combination(A)
comb_A_keys = list(comb_A.keys())
comb_A_keys.sort()
for i in range(len(B)):
    num = B[i]
    answer += find(comb_A_keys, num)
    for j in range(i):
        num = B[i] - B[j]
        answer += find(comb_A_keys, num)

print(answer)