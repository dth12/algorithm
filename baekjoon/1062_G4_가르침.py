from itertools import combinations
N, K = map(int, input().split())

word_list = ['' for _ in range(N)]
for i in range(N):
    word_list[i] = input()

learned = {'a', 'n', 't', 'i', 'c'}
alpha = set()

for word in word_list:
    for char in word:
        if char not in learned:
            alpha.add(char)


if K <= 4:
    print(0)
elif K == 5:
    cnt = 0
    for word in word_list:
        flag = 1
        for i in range(4, len(word) - 4):
            if word[i] not in learned:
                flag = 0
                break

        if flag: cnt += 1

    print(cnt)
elif len(alpha) <= K - 5:
    print(N)
else:
    max_val = 0
    for alpah_list in combinations(alpha, K - 5):
        cnt = 0
        for word in word_list:
            flag = 1
            for i in range(4, len(word) - 4):
                if word[i] not in alpah_list and word[i] not in learned:
                    flag = 0
                    break

            if flag: cnt += 1

        max_val = max(cnt, max_val)

    print(max_val)
