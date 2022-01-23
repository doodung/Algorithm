# 2667 단지번호붙이기
from collections import deque


def bfs(i, j):
    count = 1
    queue = deque()
    queue.append((i, j))
    board[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    answer.append(count)


answer = []
N = int(input())
board = [list(map(int, input())) for _ in range(N)]
cnt = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)
answer.sort()
for i in answer:
    print(i)
