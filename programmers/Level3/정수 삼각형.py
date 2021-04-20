def solution(triangle):
    for i in range(1, len(triangle)):
        L = len(triangle[i])
        for j in range(L):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == L - 1:
                triangle[i][j] += triangle[i-1][L-2]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                

    return max(triangle[-1])