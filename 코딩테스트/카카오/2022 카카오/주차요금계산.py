import math

def solution(fees, records):
    free_time, free_coin, dan_time, dan_coin = fees
    temp = {}
    dic = {}
    for r in records:
        time, num, status = map(str, r.split())
        time = int(time[:2]) * 60 + int(time[3:])

        if status == 'IN':
            temp[num] = time
        elif status == 'OUT':
            if num in dic:
                dic[num] += time - temp[num]
            else:
                dic[num] = (time - temp[num])
            del temp[num]

    for num, time in temp.items():
        if num in dic:
            dic[num] += 1439 - temp[num]
        else:
            dic[num] = 1439 - temp[num]

    answer = []
    dic = sorted(list(dic.items()), key=lambda x: x[0])
    t = 0
    for i in range(len(dic)):
        if dic[i][1] <= free_time:
            answer.append(free_coin)
        else:
            t = dic[i][1] - free_time
            answer.append((math.ceil(t / float(dan_time))) * dan_coin + free_coin)
    return answer
