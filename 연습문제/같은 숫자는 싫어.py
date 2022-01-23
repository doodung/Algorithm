def solution(s):
    answer = ''
    half = len(s) // 2
    if (len(s) % 2 == 0):
        answer = s[half - 1:half + 1]
    else:
        answer = s[half:half + 1]

    return answer