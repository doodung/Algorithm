import sys
from collections import deque

# 곳감(모래시계)
#sys.stdin = open("input.txt", "rt")
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
change = [list(map(int, input().split())) for _ in range(M)]

for i in range(len(change)):
    q = deque(board[change[i][0] - 1])
    if change[i][1] == 0:
        q.rotate(-change[i][2])
    elif change[i][1] == 1:
        q.rotate(change[i][2])
    board[change[i][0] - 1] = list(q)

S = 0
E = N - 1
sum_gam = 0

for i in range(0, N, 1):
    for j in range(S, E + 1):
        sum_gam += board[i][j]
    if i < N // 2:
        S += 1
        E -= 1
    else:
        S -= 1
        E += 1
print(sum_gam)
