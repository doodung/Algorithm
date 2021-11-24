def solution(numbers, hand):
    answer = ''
    left = ['*']
    right = ['#']
    temp = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ['*', 0, '#']]
    idx2 = 3
    idy2 = 0
    idx3 = 2
    idy3 = 3

    for i in range(len(numbers)):
        if (numbers[i] in ([i[0] for i in temp])):
            left.append(numbers[i])
            answer += 'L'
        elif (numbers[i] in ([i[2] for i in temp])):
            right.append(numbers[i])
            answer += 'R'
        else:
            for x in range(len(temp)):
                for y in range(len(temp[x])):
                    if (numbers[i] == temp[x][y]):
                        idx1 = x
                        idy1 = y
                    if (left[-1] == temp[x][y]):
                        idx2 = x
                        idy2 = y
                    if (right[-1] == temp[x][y]):
                        idx3 = x
                        idy3 = y

            leftlen = abs(idx1 - idx2) + abs(idy1 - idy2)
            rightlen = abs(idx1 - idx3) + abs(idy1 - idy3)

            if (leftlen == rightlen):
                if (hand == 'right'):
                    right.append(numbers[i])
                    answer += 'R'
                else:
                    left.append(numbers[i])
                    answer += 'L'
            if (leftlen > rightlen):
                right.append(numbers[i])
                answer += 'R'
            if (leftlen < rightlen):
                left.append(numbers[i])
                answer += 'L'
    return answer