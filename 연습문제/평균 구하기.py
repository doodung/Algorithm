def solution(num):
    answer = 0

    while (1):
        if (answer == 500):
            answer = -1
            return answer
        if (num == 1):
            break
        if (num % 2 == 0):
            num = num / 2
            answer += 1
            continue
        elif (num % 2 == 1):
            num = num * 3 + 1
            answer += 1
            continue

    return answer