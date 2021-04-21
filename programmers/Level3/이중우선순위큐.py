from heapq import heappush, heappop
'''
for num in nums:
  heapq.heappush(heap, (-num, num))
'''
def solution(operations):
    min_heap = []
    max_heap = []
    
    l = 0
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heappush(min_heap, num)
            heappush(max_heap, (-num, num))
            l += 1
        elif op == 'D':
            if l:
                if num == 1:
                    heappop(max_heap)
                    l -= 1
                elif num == -1:
                    heappop(min_heap)
                    l -= 1
            
            if l == 0:
                min_heap = []
                max_heap = []
    
    if l:
        MIN = heappop(min_heap)
        MAX = heappop(max_heap)
        return [MAX[1], MIN]
    else:
        return [0, 0]