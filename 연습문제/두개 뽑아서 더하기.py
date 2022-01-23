def solution(numbers):
    answer = []
    set_answer = set(answer)
    number = numbers
    i = 0
    j = 0

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(number)):
            answer.append(numbers[i] + number[j])

    set_answer = sorted(set(answer))

    return list(set_answer)