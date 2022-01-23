def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if (i != " "):
            if (idx % 2 == 0):
                answer += i.upper()
            else:
                answer += i.lower()
            idx += 1
        else:
            answer += ' '
            idx = 0

    print(answer)
    return answer