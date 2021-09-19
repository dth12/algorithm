def find_score(score: int) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    N = len(scores)
    answer = ''
    new_scores = [list(score) for score in zip(*scores)]
    for i in range(N):
        max_val = max(new_scores[i])
        min_val = min(new_scores[i])
        total = sum(new_scores[i])

        if new_scores[i].count(max_val) == 1 and new_scores[i][i] == max_val:
            answer += find_score((total - max_val) / (N - 1))
        elif new_scores[i].count(min_val) == 1 and new_scores[i][i] == min_val:
            answer += find_score((total - min_val) / (N - 1))
        else:
            answer += find_score(total / N)

    return answer