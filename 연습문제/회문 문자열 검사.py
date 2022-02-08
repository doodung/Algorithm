import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())

for i in range(N):
    text = str(input())
    text = text.lower()
    turn = text[::-1]
    if text == turn:
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))