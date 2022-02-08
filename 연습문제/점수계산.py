import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
test = list(map(int, input().split()))
cnt = 0
answer = 0

for i in range(N):
    if test[i] == 0:
        cnt = 0
    if test[i] == 1:
        cnt += 1
        answer += cnt

print(answer)
