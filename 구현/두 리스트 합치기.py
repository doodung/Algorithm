import sys

#sys.stdin = open("input.txt", "rt")
n1 = input()
arr1 = list(map(int, input().split()))
n2 = input()
arr2 = list(map(int, input().split()))

answer = arr1 + arr2

for i in range(len(answer)):
    print(sorted(answer)[i], end=' ')
