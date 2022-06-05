def merge_sort(arr):
    if len(arr) > 1:  # 더 이상 나눌 수 없을 때까지 나눠주는 반복문
        n = len(arr) // 2
        arr1, arr2 = arr[:n], arr[n:]
        merge_sort(arr1)
        merge_sort(arr2)
        i, j, k = 0, 0, 0  # 3개의 배열을 indexing하기 위한 변수들을 설정
        # 이 반복문에서 이해하면 좋을 점은 arr1과 arr2는
        # 이미 최소단위에서 병합될 때부터 정렬되어온 배열이라는 점입니다.
        while j < len(arr1) and k < len(arr2):
            if arr1[j] > arr2[k]:
                arr[i] = arr2[k]
                k += 1
            else:
                arr[i] = arr1[j]
                j += 1
            i += 1
        arr[i:] = arr1[j:] if j != len(arr1) else arr2[k:]
    # 반복문의 조건에 따라서 arr1과 arr2 둘 중 하나가 끝에 다다르면 종료되므로,
    # 남은 배열을 뒤에 붙여주는 과정입니다.
    # 여기서 남은 배열은 이미 정렬되어있는 배열이기 때문에
    # 이렇게 붙여주어도 정렬에는 문제가 없는 것입니다.
