import sys

#sys.stdin = open("input.txt", "rt")
N = input()
answer = ""
cnt = 0

for i in N:
    if i.isdigit():
        answer += i

answer = int(answer)

for i in range(1, answer+1):
    if answer % i == 0:
        cnt += 1

print(answer)
print(cnt)
