def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
