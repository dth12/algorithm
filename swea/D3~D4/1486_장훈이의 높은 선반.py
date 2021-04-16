import sys
sys.stdin = open("input.txt", "r")


# 가능한 점수 문제와 완전히 동일함.
# Backtracking을 통해서도 문제를 해결할 수 있음.
for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()

    visited = [0] * (sum(weights) + 1)
    cases = [0]
    answer = B + 10000000000
    for weight in weights:
        L = len(cases)
        for i in range(L):
            new = cases[i] + weight
            if not visited[new]:
                visited[new] = 1
                cases.append(new)
                if new >= B:
                    answer = min(new, answer)

    print('#{} {}'.format(tc, answer-B))

