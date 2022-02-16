import sys

# 봉우리
#sys.stdin = open("input.txt", "rt")
N = int(input())
board = [[0] * N]
for i in range(N):
    board[i].append(0)
    board.append(list(map(int, input().split())))
    board[i].insert(0, 0)
board[N].insert(0, 0)
board[N].append(0)
board.append([0] * (N + 2))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        center = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < (N + 2) and 0 <= ny < (N + 2):
                if board[nx][ny] < center:
                    cnt += 1
        if cnt == 4:
            answer += 1
        cnt = 0
print(answer)
