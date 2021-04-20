import sys
sys.stdin = open("input.txt", "r")
'''
    - 이것도 재현님 코드를 보고 배웠다.
    - 당시에 굉장히 헤매다가 backtracking을 이렇게 할 수 있구나 생각했다.
    - 다른 방법은 딱히 생각나지 않는 문제.
    - 처음에는 함수 인자로 다시 재귀를 돌리는 개념이 어려웠는데, 이제는 안 쓰면 어색한 수준이다.
    - 이제는 DFS와 BF에 아주 익숙해졌다. 거의 생각하지 않고도 코드를 쓸 수 있을 정도.
    
    이후 방향
    - 이제 BFS DFS BF에 어느정도 익숙해졌기에, 관련된 다른 알고리즘들을 찾아보는 것도 좋을 것 같다.
    - 어제 문제를 풀다, 최소스패닝트리에 대해서도 배웠는데 아직도 모르는 개념이 너무 많다.
    - 더욱 더 깊게 찾아보자


    쉬운 백트래킹 문제.
    1. dfs를 돌며, 방문되지 않은 곳만 방문하며 내려감.
    2. 만약, total 값이 이미 설정된 MIN 값보다 크면 가지치기
    3. 만약 끝까지 도달하면 작은 값을 저장.
'''
def dfs(row, total):
    global MIN
    if total > MIN:
        return
    elif row == N:
        MIN = min(total, MIN)
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(row+1, total+board[row][i])
                visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MIN = 11 * 10
    visited = [0 for _ in range(N)]
    dfs(0, 0)
    print('#{} {}'.format(tc, MIN))
