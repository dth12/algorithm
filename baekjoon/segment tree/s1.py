def is_right(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True


def is_balance(p):
    if p.count('(') == p.count(')'):
        return True
    else:
        return False


def is_divide(p):
    u = ''
    v = ''
    for i in range(len(p)):
        u += p[i]
        if is_balance(u):
            v = p[i + 1:]
            break

    return u, v


def is_not_right(u, v):
    w = '('
    w += solution(v)
    w += ')'
    uu = ''
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            uu += ')'
        else:
            uu += '('

    return w + uu


def solution(p):
    if p == '':
        return p
    elif is_right(p):
        return p
    else:
        u, v = is_divide(p)
        if is_right(u):
            return u + solution(v)
        else:
            return is_not_right(u, v)


print(solution("()))((()"))