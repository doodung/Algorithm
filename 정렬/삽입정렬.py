def insert_sort(arr):
    for i in range(1, len(arr)):
        memory = arr[i]
        j = i - 1
        while j >= 0 and memory < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = memory
