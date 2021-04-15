def powerset(idx, total):
    if idx == N:
        possible[idx].add(total)
        return
    else:
        if total in possible[idx]:
            return
        else:
            possible[idx].add(total)
        powerset(idx+1, total+scores[idx])
        powerset(idx+1, total)


T = int(input())

for tc in range(1, T+1):
    # 문제의 개수
    N = int(input())
    scores = list(map(int, input().split()))
    possible = [set() for _ in range(N+1)]
    powerset(0, 0)
    print('#{} {}'.format(tc, len(possible[N])))


# DP

T = int(input())

for tc in range(1, T+1):
    # 문제의 개수
    N = int(input())
    scores = list(map(int, input().split()))
    possible = [0] * (sum(scores) + 1)
    cases = [0]
    possible[0] = 1

    for score in scores:
        for i in range(len(cases)):
            new = cases[i] + score
            if not possible[new]:
                possible[new] = 1
                cases.append(new)

    print('#{} {}'.format(tc, sum(possible)))
