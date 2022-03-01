def solution(sizes):
    answer = 0
    m1 = 0
    m2 = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    for i in range(len(sizes)):
        if m1 < sizes[i][0]:
            m1 = sizes[i][0]
        if m2 < sizes[i][1]:
            m2 = sizes[i][1]

    answer = m1 * m2
    return answer