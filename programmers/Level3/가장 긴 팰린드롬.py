def solution(s):
    answer = 1

    for i in range(1, len(s) - 1):

        # 홀수
        repeat_odd = 1
        for j in range(1, min(i + 1, len(s) - i)):
            if s[i - j] == s[i + j]:
                repeat_odd += 2
            else:
                break

        # 짝수
        repeat_even = 0
        for k in range(min(i+1, len(s) - i - 1)):
            if s[i - k] == s[i + k + 1]:
                repeat_even += 2
            else:
                break

        answer = max(repeat_even, repeat_odd, answer)

    return answer
