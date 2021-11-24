def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0
    dic = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    for i in win_nums:
        if i in lottos:
            lottos.remove(i)
            count = count + 1

    zero_count = lottos.count(0)
    answer = [dic[count + zero_count], dic[count]]

    return answer