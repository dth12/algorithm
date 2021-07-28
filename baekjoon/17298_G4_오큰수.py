import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(N)]
heap = []

for i in range(N):
    if len(heap):
        while heap:
            num = heappop(heap)
            if num[0] < arr[i]:
                answer[num[1]] = arr[i]
            else:
                heappush(heap, num)
                break

    heappush(heap, [arr[i], i])

print(*answer)

