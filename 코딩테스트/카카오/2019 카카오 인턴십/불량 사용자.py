def solution(user_id, banned_id):
    answer = []
    temp = [[]]
    for bi in banned_id:
        t = []
        for ui in user_id:
            if len(ui) != len(bi):
                continue
            flag = True
            for i in range(len(ui)):
                if bi[i] != '*' and bi[i] != ui[i]:
                    flag = False
                    break
            if flag:
                for k in temp:
                    if ui not in k:
                        t.append(k + [str(ui)])

        temp = t
    for k in temp:
        if set(k) not in answer:
            answer.append(set(k))

    return len(answer)