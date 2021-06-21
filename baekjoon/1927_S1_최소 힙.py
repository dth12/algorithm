from math import log, ceil
import sys
input = sys.stdin.readline

def heappush(num: int):
    global heap_count
    heap_count += 1
    heap[heap_count] = num

    child = heap_count
    parent = heap_count // 2
    while parent >= 1:
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent //= 2
        else:
            break


def heappop():
    global heap_count
    if heap_count == 0:
        return 0

    if heap_count == 3:
        debug = True

    return_val = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    parent = 1
    if heap[3] and heap[2] > heap[3]:
        child = 3
    else:
        child = 2

    while child < heap_count and heap[parent] > heap[child]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child *= 2

        if heap[child + 1] and heap[child] > heap[child + 1]:
            child += 1

    heap_count -= 1
    return return_val


N = int(input())
heap_count = 0
exponent = ceil(log(N, 2)) + 1
heap = [0] * (2 ** exponent)
for _ in range(N):
    target = int(input())
    if target:
        heappush(target)
    else:
        print(heappop())

    # print(heap)

'''
36
0
9
8
7
6
5
4
3
2
1
11
13
14
15
16
18
100
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

'''






