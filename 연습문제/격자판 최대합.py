import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
answer = []
cross = 0

for i in range(N):
    answer.append(sum(board[i]))
    cross += board[i][i]
answer.append(cross)

cross = 0
for i in range((N - 1), -1, -1):
    cross += board[i][N - i - 1]
answer.append(cross)

for j in range(N):
    plus = 0
    for i in range(N):
        plus += board[i][j]
    answer.append(plus)

print(max(answer))
