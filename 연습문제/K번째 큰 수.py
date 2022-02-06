import sys
from itertools import combinations

#sys.stdin = open("input.txt", "rt")
N, K = map(int, input().split())
temp = list(map(int, input().split()))
answer = list(combinations(temp, 3))
h = []
for i in range(len(answer)):
    h.append(sum(answer[i]))

set_h = list(set(h))
set_h.sort(reverse=True)
print(set_h[K - 1])
