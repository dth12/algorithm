import sys
sys.stdin = open('input.txt', 'r')

'''
    1. n + m분 동안 같이 작업
    2. 1분마다 한 라인 수정
    3. 1분마다 마지막에 한 라인 추가 또는 원래있던 파일 수정
    4. 이미 k줄 작성
    5. 시퀀스대로 작성.
    6. 실제 시퀀스를 찾아라.
'''

def solve(lines: int) -> list:
    current_lines = lines
    answer = []
    idx1 = 0
    idx2 = 0
    flag = 1

    while flag:

        flag = 0

        if idx1 < len(A):
            if A[idx1] == 0:
                current_lines += 1
                answer.append(0)
                idx1 += 1
                flag = 1
            elif 0 < A[idx1] <= current_lines:
                answer.append(A[idx1])
                idx1 += 1
                flag = 1

        if idx2 < len(B):
            if B[idx2] == 0:
                current_lines += 1
                answer.append(0)
                flag = 1
                idx2 += 1
            elif 0 < B[idx2] <= current_lines:
                answer.append(B[idx2])
                flag = 1
                idx2 += 1

    if len(answer) == n + m:
        return answer
    else:
        return [-1]


T = int(input())
for tc in range(1, T + 1):
    blank = input()
    lines, n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int,input().split()))
    print(*solve(lines))
