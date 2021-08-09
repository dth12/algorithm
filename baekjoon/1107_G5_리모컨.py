target = list(map(int, input().split()))
M = int(input())
broken = list(map(int, input().split()))
button = []

for i in range(10):
    if i in broken: continue
    button.append(i)

for i in range(10):

