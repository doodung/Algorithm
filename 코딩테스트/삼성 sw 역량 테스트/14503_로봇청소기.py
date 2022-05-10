# 14503 로봇청소기
from collections import deque

N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robot_x, robot_y, robot_dir = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def BFS(x, y, dir):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    clean = 1
    while q:
        x, y = q.popleft()
        turn = 0
        for _ in range(4):
            dir = (dir + 3) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
            if not visited[nx][ny] and board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
                clean += 1
                break
            else:
                turn += 1
        if turn == 4:
            x -= dx[dir]
            y -= dy[dir]
            if board[x][y] == 1:
                break
            q.append((x, y))
    return clean


print(BFS(robot_x, robot_y, robot_dir))
