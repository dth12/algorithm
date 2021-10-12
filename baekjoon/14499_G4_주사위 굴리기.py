def inrange(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C


R, C, X, Y, K = map(int, input().split())
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
board = [list(map(int, input().split())) for _ in range(R)]
commands = list(map(int, input().split()))

dice = [[i, 0] for i in range(6)]
roll = {
    4:
        {
            4: 0,
            2: 2,
            3: 3,
            5: 4,
            1: 5,
            0: 1,
        },
    3:
        {
            1: 0,
            2: 2,
            3: 3,
            4: 5,
            0: 4,
            5: 1,
        },
    1:
        {
            3: 0,
            0: 2,
            2: 5,
            1: 1,
            4: 4,
            5: 3,
        },
    2:
        {
            2: 0,
            3: 5,
            0: 3,
            1: 1,
            4: 4,
            5: 2,
        }
}
pos = [X, Y]
for command in commands:
    r, c = pos
    nr = r + dr[command]
    nc = c + dc[command]

    if not inrange(nr, nc): continue
    top = -1
    bottom = -1
    for i in range(6):
        num = roll[command][dice[i][0]]
        dice[i][0] = num

        if num == 0:
            bottom = i

        if num == 5:
            top = i

    if board[nr][nc] == 0:
        board[nr][nc] = dice[bottom][1]
    else:
        dice[bottom][1] = board[nr][nc]
        board[nr][nc] = 0

    print(dice[top][1])
    pos = [nr, nc]
