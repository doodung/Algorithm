def select_sort(arr):
    for j in range(len(arr)):
        index = j
        for i in range(1 + j, len(arr)):
            if arr[i] < arr[index]:
                index = i
        arr[j], arr[index] = arr[index], arr[j]
