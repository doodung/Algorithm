from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    answer = []
    flag = False
    N = int(input())
    temp = str(N)
    l = len(temp)
    permu = list(permutations(temp, l))
    for i in range(len(permu)):
        answer.append(int("".join(permu[i])))
    answer = set(answer)
    answer = list(answer)
    for j in range(len(answer)):
        if answer[j] % N == 0 and answer[j]!=N:
            flag = True
    if flag:
        print("#%d possible" % test_case)
    else:
        print("#%d impossible" % test_case)