from collections import deque


def inrange(r: int, c: int, R: int, C: int) -> bool:
    return 0 <= r < R and 0 <= c < C


def find_block(table: list) -> list:
    R = C = len(table)
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    blocks = []
    for row in range(R):
        for col in range(C):
            if visited[row][col] or table[row][col] == 0: continue
            Q = deque([[row, col]])
            path = {(0, 0)}
            while Q:
                r, c = Q.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if inrange(nr, nc, R, C) and table[nr][nc] and not visited[nr][nc]:
                        path.add((nr - row, nc - col))
                        Q.append([nr, nc])
                        visited[nr][nc] = 1

            if len(path):
                blocks.append(path)

    return blocks


def find_empty(board: list, row: int, col: int) -> set:
    Q = deque([[row, col]])
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    path = {(0, 0)}
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc, len(board), len(board)) and not visited[nr][nc] and board[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append([nr, nc])
                path.add((nr - row, nc - col))

    return path


def solve(blocks: list, board: list) -> int:
    N = len(board)
    answer = 0
    visited = [0 for _ in range(len(blocks))]
    for _ in range(4):
        for r in range(N):
            for c in range(N):
                if board[r][c]: continue
                path = find_empty(board, r, c)
                for idx, block in enumerate(blocks):
                    if visited[idx]: continue
                    cnt = 0
                    for pos in block:
                        if pos in path:
                            cnt += 1

                    if cnt == len(block) and cnt == len(path):
                        visited[idx] = 1
                        for row, col in path:
                            board[r + row][c + col] = 1
                            answer += 1

                        break

        board = [list(line)[::-1] for line in zip(*board)]

    return answer


def solution(game_board, table):
    blocks = find_block(table)
    answer = solve(blocks, game_board)
    return answer