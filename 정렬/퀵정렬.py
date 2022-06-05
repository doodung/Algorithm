def quick_sort(arr):
    if not arr:
        return arr
    num = arr.pop()  # 임의로 하나의 피벗 지정. 해당 경우는 배열의 마지막 원소
    left = []
    right = []
    for i in range(len(arr)):  # 반복문을 사용해서 피벗 기준으로 배열을 2개로 나눔
        if arr[i] > num:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return quick_sort(left) + [num] + quick_sort(right)
    # 재귀를 이용하여 정렬 완성
