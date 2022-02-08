import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
numList = list(map(str, input().split()))


def reverse(x):
    temp = x[::-1]
    return temp


def isPrime(x):
    if x == 1:
        return False
    for j in range(2, x // 2 + 1):
        if x % j == 0:
            return False
    else:
        return True


for i in range(N):
    res = int(reverse(numList[i]))
    if isPrime(res):
        print(res, end=' ')
