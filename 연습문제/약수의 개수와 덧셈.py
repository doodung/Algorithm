def solution(left, right):
    answer = [0] * (right + 1)
    l = right - left

    for i in range(left, right + 1):
        answer[i] = 1
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                answer[i] += 1

    cnt = 0
    for i in range(len(answer)):
        if answer[i] == 0:
            continue
        elif answer[i] % 2 == 0:
            cnt += i
        elif answer[i] % 2 == 1:
            cnt -= i

    return cnt