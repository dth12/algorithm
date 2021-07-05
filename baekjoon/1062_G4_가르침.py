N, K = map(int, input().split())

if K <= 4:
    print(0)
else:
    learned = {'a', 't', 'n', 'i', 'c'}
    alpha_dict = {}
    K -= 5
    for i in range(N):
        word = input()
        L = len(word)
        for char in word[4:L - 4]:
            if char in learned:
                continue
            if char not in alpha_dict:
                alpha_dict[char[i]] = [False] * N
            alpha_dict[char[i]] = True

    