import sys
#sys.stdin = open("input.txt", "rt")
T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    array = list(map(int, input().split()))

    temp = array[s - 1:e]
    temp.sort()
    print("#%d" % (i+1), temp[k - 1])
