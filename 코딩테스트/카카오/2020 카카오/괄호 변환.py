def solution(p):
    # 1
    if not p:
        return ''

    # 2
    u, v = divide(p)

    # 3
    if check(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'

        # 4-4
        for s in u[1:len(u) - 1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('

        # 4-5
        return answer


def check(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def divide(str):
    left = 0
    right = 0
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return str[:i + 1], str[i + 1:]

