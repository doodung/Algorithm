from collections import deque

def solution(numbers, target):
    answer = 0
    deq = deque() 
    l = len(numbers)
    deq.append([-numbers[0], 0])
    deq.append([+numbers[0], 0])
    while deq :
        num, i = deq.popleft()
        if i+1 == l :
            if num == target : answer += 1
        else :
            deq.append([num - numbers[i + 1], i + 1])
            deq.append([num + numbers[i + 1], i + 1])
    return answer