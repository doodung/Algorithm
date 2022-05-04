def solution(numbers, hand):
    answer = ''
    prev = ''
    last_L = '*'
    last_R = '#'
    L = [1, 4, 7]
    R = [3, 6, 9]
    E = [2, 5, 8, 0]
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in numbers:
        if i in L:
            answer += 'L'
            last_L = i
        if i in R:
            answer += 'R'
            last_R = i
        if i in E:
            for j in range(len(pad)):
                for k in range(3):
                    if pad[j][k] == i:
                        index = [j, k]
                    if pad[j][k] == last_L:
                        index_L = [j, k]
                    if pad[j][k] == last_R:
                        index_R = [j, k]
            chai_L = abs(index[0] - index_L[0]) + abs(index[1] - index_L[1])
            chai_R = abs(index[0] - index_R[0]) + abs(index[1] - index_R[1])
            if chai_L < chai_R:
                last_L = i
                answer += 'L'
            if chai_R < chai_L:
                last_R = i
                answer += 'R'
            if chai_R == chai_L:
                if hand == 'right':
                    last_R = i
                    answer += 'R'
                else:
                    last_L = i
                    answer += 'L'

    return answer