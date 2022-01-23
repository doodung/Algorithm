def solution(arr):
    temp = arr
    small = min(arr)

    while (1):
        if small in temp:
            temp.remove(small)
        else:
            break

    if len(temp) == 0:
        temp.append(-1)

    return temp