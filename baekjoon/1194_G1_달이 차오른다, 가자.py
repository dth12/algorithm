N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def bfs() -> None:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    