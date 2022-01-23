def solution(phone_number):
    answer = ''
    length = len(phone_number)
    answer += ((length - 4) * '*') + phone_number[length - 4:length + 1]

    return answer