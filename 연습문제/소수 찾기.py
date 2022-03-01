def solution(n):
    answer = [0]*(n+1)
    cnt = 0

    for i in range(2, n + 1):
        if answer[i] == 0:
            cnt += 1
            for j in range(i, n + 1, i):
                answer[j] = 1
    return cnt