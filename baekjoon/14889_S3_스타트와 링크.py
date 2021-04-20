def powerset(idx):
    global MIN
    val = sum(sel)

    if idx == N:
        link = []
        start = []
        if val == N//2:
            for i in range(N):
                if sel[i]:
                    link.append(i)
                else:
                    start.append(i)

            link_total = 0
            start_total = 0
            for i in range(N//2):
                for j in range(N//2):
                    link_total += graph[link[i]][link[j]]
                    start_total += graph[start[i]][start[j]]
            
            MIN = min(abs(link_total-start_total), MIN)
        else:
            return
    else:
        sel[idx] = 0
        powerset(idx+1)
        sel[idx] = 1
        powerset(idx+1)


MIN = 100000000
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
sel = [0] * N
powerset(0)
print(MIN)