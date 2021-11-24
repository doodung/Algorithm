import re

def solution(new_id):
    answer = ''
    s = ''
    dot = '.'
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9-_.]', '', answer)
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if len(answer) == 0:
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if (answer[-1] == '.'):
            answer = answer.strip('.')
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer