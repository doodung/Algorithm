def solution(participant, completion):
    answer = ''
    dic = []
    name_dic = {}
    key = []

    for name in participant:
        if name in name_dic:
            name_dic[name] += 1
        else:
            name_dic[name] = 1

    for i in completion:
        name_dic[i] = name_dic.get(i) - 1

    for j in participant:
        if name_dic[j] == 1:
            answer = j

    return answer