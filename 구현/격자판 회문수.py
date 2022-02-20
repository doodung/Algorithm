import sys

# 격자판 회문수
# sys.stdin = open("input.txt", "r")
board = [list(map(str, input().split())) for i in range(7)]
cnt = 0


def check(a):
    reverse = a[::-1]
    if a == reverse:
        return 1
    else:
        return 0


for i in range(7):
    for j in range(3):
        cnt += check(board[i][j:j + 5])

temp = []
for i in range(7):
    for j in range(5):
        temp.append(board[j][i])
    cnt += check(temp)
    temp = []
    for j in range(1, 6):
        temp.append(board[j][i])
    cnt += check(temp)
    temp = []
    for j in range(2, 7):
        temp.append(board[j][i])
    cnt += check(temp)
    temp = []

print(cnt)
