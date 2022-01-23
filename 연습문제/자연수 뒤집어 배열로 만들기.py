def solution(n):
    answer = ''
    answer = str(n)
    re = 0

    for i in range(0, len(answer)):
        re += int(answer[i:i + 1])
    return re