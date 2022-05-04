def solution(s):
    answer = []
    s = s[2:-2]
    temp = map(str, s.split('},{'))
    for i in range(len(temp)):
        t = list(map(int, temp[i].split(',')))
        answer.extend(t)

    A = []
    T = []
    for j in answer:
        if j not in T:
            T.append(j)
            A.append([answer.count(j), j])

    A.sort(reverse=True)
    result = []
    for i in range(len(A)):
        result.append(A[i][1])
    return result