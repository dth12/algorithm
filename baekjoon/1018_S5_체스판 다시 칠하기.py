R, C = map(int, input().split())
board = [input() for _ in range(R)]

color = ['W', 'B']
answer = 64
for r in range(R - 7):
    for c in range(C - 7):
        for i in range(2):
            flag = i
            temp = 0
            for dr in range(8):
                for dc in range(8):
                    if board[r + dr][c + dc] != color[flag]:
                        temp += 1
                    if dc == 7: continue
                    flag = 0 if flag else 1

            answer = min(answer, temp)

print(answer)
