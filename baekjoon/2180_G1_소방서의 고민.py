import sys
input = sys.stdin.readline


def compare(x: list, y: list) -> int:
    a1, b1 = x
    a2, b2 = y

    if a1 == 0:
        return False
    elif a2 == 0:
        return True
    elif a1 > 0 and a2 > 0:
        return b1 / a1 < b2 / a2
    elif b1 == 0 and b2 == 0:
        return a1 < a2


def merge_sort(start: int, end: int) -> None:
    if start < end:
        pivot = (start + end) // 2
        merge_sort(start, pivot)
        merge_sort(pivot + 1, end)
        merge(start, end)


def merge(start: int, end: int) -> None:
    pivot = (start + end) // 2
    idx1 = start
    idx2 = pivot + 1
    temp = []
    while idx1 <= pivot and idx2 <= end:
        if compare(times[idx1], times[idx2]):
            temp.append(times[idx1])
            idx1 += 1
        else:
            temp.append(times[idx2])
            idx2 += 1

    while idx1 <= pivot:
        temp.append(times[idx1])
        idx1 += 1

    while idx2 <= end:
        temp.append(times[idx2])
        idx2 += 1

    for i in range(start, end+1):
        times[i] = temp[i - start]


N = int(input())
times = []

for i in range(N):
    a, b = list(map(int, input().split()))
    times.append([a, b])

merge_sort(0, len(times) - 1)
time = 0
for a, b in times:
    time += (a * time + b)
    time %= 40000

print(time)





