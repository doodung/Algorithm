from collections import deque
import math


def solution(progresses, speeds):
    deq = deque()
    answer = deque()
    max_num = 0

    for i in range(len(progresses)):
        deq.append(int(math.ceil((100 - progresses[i]) / float(speeds[i]))))
        if (deq[i] > max_num):
            max_num = deq[i]
            answer.append(1)
        else:
            answer[-1] += 1

    return list(answer)