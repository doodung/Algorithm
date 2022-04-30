# 1. 조합 경우의 수
def get_combinations(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in get_combinations(rest_arr, n - 1):
            result.append([elem] + C)
    return result


print("조합 출력", get_combinations([1, 2, 3, 4, 5], 3))


# 단순 조합 경우의 수
def choose(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n - 1, k - 1) + choose(n - 1, k)


# 조합 경우의 수
print("조합 경우의 수", choose(10, 2))


# 순열 1
# 배열의 원소로 새로운 순열을 반환한다.
def get_permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in get_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]
    return result


arr = [0, 1, 2, 3, 4, 5]
print("순열 출력", get_permutations(arr, 3))

# 순열 2
def get_permutations2(n,depth,P):
    result=[]
    if depth==n:
        return [P]
    else:
        for i in range(len(arr)):
            if chosen[i] == True:
                continue
            chosen[i]=True
            result += get_permutations2(n,depth+1,P+[i])
            chosen[i]=False
    return result

arr=[0,1,2,3,4]
chosen = [False for _ in range(len(arr))]
print("배열의 인덱스로 새로운 순열 만들기", get_permutations2(3,0,[]))