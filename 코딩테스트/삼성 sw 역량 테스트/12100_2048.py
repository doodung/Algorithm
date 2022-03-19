import sys
from collections import deque

# 12100 2048
# 2022-03-19 doodung

sys.stdin = open("input.txt.", "r")
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
print(board)
Max = -1
answer, q = 0, deque()


def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0


def merge(i, j, dx, dy):
    while q:
        x = q.popleft()
        # 0이라면 그대로 놓음
        if not board[i][j]:
            board[i][j] = x
        # 값이 일치하면 2배
        elif board[i][j] == x:
            board[i][j] = x * 2
            i, j = i + dx, j + dy
        # 값이 일치하지 않으면 그자리에 그대로 둠
        else:
            i, j = i + dx, j + dy
            board[i][j] = x


def move(k):
    # 위로 이동
    if k == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    # 아래로 이동
    elif k == 1:
        for j in range(N):
            for i in range(N - 1, -1, -1):
                get(i, j)
            merge(N - 1, j, -1, 0)
    # 오른쪽으로 이동
    elif k == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    # 왼쪽으로 이동
    else:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                get(i, j)
            merge(i, N - 1, 0, -1)


def recursive(count):
    global board, answer
    if count == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4):
        move(k)
        # 재귀호출
        recursive(count + 1)
        # 백트래킹 할떄 이전 보드의 상태를 기억하기 위함
        board = [x[:] for x in b]


recursive(0)
print(answer)
