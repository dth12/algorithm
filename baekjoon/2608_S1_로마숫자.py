def rome_to_number(rome_num: str) -> int:
    flag = 0
    num = 0
    for i in range(0, len(rome_num) - 1):
        if flag:
            flag = 0
            continue

        temp1 = rome_num[i]
        temp2 = rome_num[i + 1]
        if temp1 + temp2 in rome_num_dict:
            num += rome_num_dict[temp1 + temp2]
            flag = 1
        else:
            num += rome_num_dict[temp1]

    if not flag:
        num += rome_num_dict[rome_num[len(rome_num) - 1]]

    return num


rome_num_1 = input()
rome_num_2 = input()
rome_num_dict = {
    'V': 5,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
    'I': 1,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
num_rome_dict = {value: key for key, value in rome_num_dict.items()}

num = rome_to_number(rome_num_1) + rome_to_number(rome_num_2)
temp = num
answer = ''
idx = 3
while temp:
    q = temp // (10 ** idx)
    temp -= q * (10 ** idx)
    if q == 1 or q == 5 or q == 4 or q == 9:
        answer += num_rome_dict[q * (10 ** idx)]
    elif q > 5:
        answer += num_rome_dict[5 * (10 ** idx)]
        answer += num_rome_dict[10 ** idx] * (q - 5)
    elif q < 5:
        answer += num_rome_dict[10 ** idx] * q

    idx -= 1

print(num)
print(answer)



















