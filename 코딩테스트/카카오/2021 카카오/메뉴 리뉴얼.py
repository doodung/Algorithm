from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        dic = {}
        temp = []

        for j in orders:
            temp.extend(list(combinations(sorted(j), i)))

        for k in temp:
            s = ''.join(k)
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1

        for l in dic:
            if dic[l] > 1:
                if dic[l] == max(dic.values()):
                    answer.append(l)

    return sorted(answer)
