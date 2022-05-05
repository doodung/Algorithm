# 1920 수찾기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
A.sort()
flag = False

for n in num:
    start = 0
    end = N - 1
    target = n
    flag = False
    while start <= end:
        mid = (end + start) // 2
        if A[mid] == target:
            print(1)
            flag = True
            break
        elif A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if not flag:
        print(0)
