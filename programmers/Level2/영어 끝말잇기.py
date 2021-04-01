def solution(n, words):
    
    repeat = {words[0]}
    answer = [0, 1]
    turn = 1
    idx = 0

    while idx < len(words)-1:
        
        word = words[idx]
        next_word = words[idx+1]
        print(answer, turn, idx)
        if len(next_word) > 1:
            if next_word not in repeat and word[len(word)-1] == next_word[0]:
                idx += 1
                turn += 1
                repeat.add(next_word)
                if turn == n + 1:
                    turn = 1
                    answer[1] += 1
            else:
                idx += 1
                turn += 1
                if turn == n + 1:
                    turn = 1
                    answer[1] += 1
                answer[0] = turn
                break
    else:     
        answer = [0, 0]
        
    return answer