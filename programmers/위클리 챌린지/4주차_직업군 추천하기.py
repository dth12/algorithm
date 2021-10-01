def solution(table, languages, preference):
    score_table = {}
    result = {'SI': 0, 'CONTENTS': 0, 'HARDWARE': 0, 'PORTAL': 0, 'GAME': 0}
    for col in table:
        lang_list = col.split()
        part = lang_list.pop(0)
        score_table[part] = {lang: 5 - idx for idx, lang in enumerate(lang_list)}

    for idx, my_lang in enumerate(languages):
        for part in score_table:
            if my_lang not in score_table[part]: continue
            temp = score_table[part][my_lang]
            result[part] += temp * preference[idx]

    result_list = [[value, key] for key, value in result.items()]
    result_list.sort(key=lambda x: (-x[0], x[1]))
    return result_list[0][1]