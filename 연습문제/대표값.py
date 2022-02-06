import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
a = list(map(int, input().split()))

ave = int(sum(a) / N + 0.5)
mini = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < mini:
        mini = tmp
        score = x
        res = idx+1
    elif tmp == mini:
        if x > score:
            score = x
            res = idx+1

print(ave, res)
