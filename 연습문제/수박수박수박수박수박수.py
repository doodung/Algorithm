def solution(n):
    answer = ''
    watermelon = '수박수박'

    if (n == 1):
        answer = '수'
    else:
        answer = watermelon * (n // 2)
        answer = answer[:n]

    return answer