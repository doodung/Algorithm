import sys

# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
cnt = [0] * (N + M + 1)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        cnt[i + j] += 1

for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i, end=' ')
