import sys

#sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
first = []
second = []
for i in range(N):
    first.append(i + 1)
for j in range(M):
    second.append(j + 1)

answer = []
temp = [0 for i in range(N + M + 1)]

for n in range(N):
    for m in range(M):
        answer.append(first[n] + second[m])

for i in range(len(answer)):
    if temp[answer[i]] == 0:
        temp[answer[i]] = 1
    else:
        temp[answer[i]] += 1

maxi = max(temp)
for k in range(len(temp)):
    if maxi == temp[k]:
        print("%d " % k, end='')
