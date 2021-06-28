import sys
input = sys.stdin.readline

N = int(input())
tables = [list(map(int, input().split())) for _ in range(N)]
tables.sort(key=lambda x: (x[1], x[0]))

cnt = 0
before_start = -1
before_end = -1
for start, end in tables:
    if start >= before_end:
        cnt += 1
        before_end = end
        before_start = start

print(cnt)
