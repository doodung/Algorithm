def solution(x):
    arr = str(x)
    temp = 0

    for i in range(len(arr)):
        temp += int(arr[i:i + 1])
    if (x % temp == 0):
        return True
    else:
        return False