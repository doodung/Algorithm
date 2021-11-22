def solution(array, commands):
    answer = []
    a = []

    for i in range(0, len(commands)):
        answer.append(array[commands[i][0] - 1:commands[i][1]])
        answer[i].sort()
        a.append(answer[i][commands[i][2] - 1])

    return a