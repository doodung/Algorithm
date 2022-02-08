import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
num = list(map(str, input().split()))
answer = 0


# 각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    res = 0
    for j in range(len(x)):
        res += int(x[j])
    return res


for i in range(N):
    temp = digit_sum(num[i])
    if temp > answer:
        answer = temp
        cnt = i

print(num[cnt])
