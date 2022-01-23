def solution(nums):
    answer = 0
    select = len(nums) // 2
    temp = list(set(nums))

    if len(temp) >= select:
        answer = select
    else:
        answer = len(temp)

    return answer
