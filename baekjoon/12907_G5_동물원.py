import sys
sys.stdin = open("input.txt", "r")

def find():
    global result
    answer_dict = {1: [], 2: []}

    if max(animal) >= len(animal):
        result = 0
        return


    for i in animal:
        if i not in answer_dict[1]:
            answer_dict[1].append(i)
        elif i not in answer_dict[2]:
            answer_dict[2].append(i)
        else:
            result = 0
            return

    answer_dict[1].sort()
    answer_dict[2].sort()

    if answer_dict[1] and answer_dict[1] != list(range(answer_dict[1][-1]+1)):
        result = 0
        return
    elif answer_dict[2] and answer_dict[2] != list(range(answer_dict[2][-1]+1)):
        result = 0
        return

    MIN = min(len(answer_dict[1]), len(answer_dict[2]))
    if len(answer_dict[1]) == len((answer_dict[2])):
        result = result * 2 ** MIN
    else:
        result = result *  2**(MIN + 1)


N = int(input())
animal = list(map(int, input().split()))
result = 1

find()
print(result)
