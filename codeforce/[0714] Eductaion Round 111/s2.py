import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    n, a, b = map(int, input().split())
    word = input()
    if b >= 0:
        print((a + b) * len(word))
    else:
        cnt0 = 0
        cnt1 = 0
        flag = 0
        for i in range(len(word)):
            if flag == 0 and word[i] == '0':
                flag = 1
                cnt0 += 1
            elif flag == 1 and word[i] == '1':
                flag = 0

        flag = 0
        for i in range(len(word)):
            if flag == 0 and word[i] == '1':
                flag = 1
                cnt1 += 1
            elif flag == 1 and word[i] == '0':
                flag = 0
        if cnt1 == cnt0:
            print(a * len(word) + b * (cnt1 + 1))
        else:
            print(a * len(word) + b * max(cnt0, cnt1))
