from itertools import combinations as comb


T = int(input())

one_digit_prime = [2, 3, 5, 7]
one_digit_no_prime = [1, 4, 6, 8, 9]
possible_two_digit_nums = [25, 27, 32, 35, 52, 57, 72, 75]

for _ in range(T):
    k = int(input())
    num_dict = {i: 0 for i in range(1, 10)}
    num = list(map(int, input()))
    flag = 0
    for i in num:
        num_dict[i] += 1
        if i in one_digit_no_prime:
            flag = i
            break

    if flag:
        print(1)
        print(flag)
    else:
        answer = 0
        for prime in one_digit_prime:
            if num_dict[prime] >= 2:
                answer = prime * 10 + prime

        if answer:
            print(2)
            print(answer)
        else:
            new_num = []
            for i in num:
                if i in one_digit_prime:
                    new_num.append(i)

            answer = 0
            for a, b in list(comb(new_num, 2)):
                answer = 10 * a + b
                if answer in possible_two_digit_nums:
                    print(2)
                    print(answer)
                    break












