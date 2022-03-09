from itertools import permutations


def solution(numbers):
    answer, num, temp = [], [], []

    for i in range(len(numbers)):
        num.append(numbers[i])

    for i in range(1, len(num) + 1):
        temp = list(permutations(num, i))
        answer.extend(temp)

    temp = []
    for i in answer:
        temp.append(int(''.join(i)))

    answer = []
    for i in range(len(temp)):
        if temp[i] != 1 and temp[i] != 0:
            if prime(temp[i]) and temp[i] not in answer:
                answer.append(temp[i])

    return len(answer)


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True