import sys
sys.stdin = open("input.txt", "r")

N = int(input())

start = 1
end = N
while True:

    pivot = (start + end)//2

    if pivot ** 2 > N:
        end = pivot
    elif pivot ** 2 < N:
        start = pivot
    elif pivot ** 2 == N:
        break

print(pivot)
