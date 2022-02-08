import sys

#sys.stdin = open("input.txt", "rt")
l = [list(map(int, input().split())) for i in range(10)]
card = [0] * 20

for i in range(20):
    card[i] = i + 1

for j in range(10):
    start = l[j][0] - 1
    end = l[j][1]
    temp = reversed(card[start:end])
    card[start:end] = temp

for k in range(20):
    print(card[k], end=' ')

