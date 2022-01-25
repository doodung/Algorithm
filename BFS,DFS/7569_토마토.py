# 7569
# 토마토

from collections import deque


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < N and -1 < ny < M and -1 < nz < H:
                if board[nz][nx][ny] == 0:
                    board[nz][nx][ny] = board[z][x][y] + 1
                    queue.append((nz, nx, ny))


def result():
    answer = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if board[i][j][k] == 0:
                    return print(-1)
                answer = max(answer, board[i][j][k])
    return print(answer - 1)


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
result()
