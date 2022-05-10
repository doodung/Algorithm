# 2573 빙산
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
age = 0


def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        water = 0
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if board[nx][ny] == 0:
                    water += 1
            new_board[x][y] = water
    return new_board


while 1:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    new_board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] > 0:
                BFS(i, j)
                cnt += 1
            if board[i][j] > 0 and new_board[i][j] > 0:
                if board[i][j] < new_board[i][j]:
                    board[i][j] = 0
                else:
                    board[i][j] -= new_board[i][j]

    if cnt == 0:
        answer = 0
        break

    if cnt >= 2:
        answer = age
        break

    age += 1

print(answer)
