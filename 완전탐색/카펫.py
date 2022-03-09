import math


def solution(brown, yellow):
    answer = []
    temp = []

    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            temp.append([yellow // i, yellow // (yellow // i)])

    for i in range(len(temp)):
        if brown == (temp[i][0] * 2) + (temp[i][1] * 2) + 4:
            answer = [temp[i][0] + 2, temp[i][1] + 2]

    return answer