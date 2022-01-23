def solution(answers):
    answer = []
    temp = []
    length = len(answers)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(0, length):
        if (answers[i] == one[i % 5]):
            score1 += 1
        if (answers[i] == two[i % 8]):
            score2 += 1
        if (answers[i] == three[i % 10]):
            score3 += 1

    temp = max(score1, score2, score3)
    if (temp == score1):
        answer.append(1)
    if (temp == score2):
        answer.append(2)
    if (temp == score3):
        answer.append(3)

    return answer