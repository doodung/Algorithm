# 1520 내리막길
import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(x, y):
    q = [(-board[x][y], x, y)]
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while q:
        h, cx, cy = heappop(q)
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if not 0 <= nx < N or not 0 <= ny < M:
                continue
            if board[cx][cy] <= board[nx][ny]:
                continue
            if visited[nx][ny] == 0:
                heappush(q, (-board[nx][ny], nx, ny))
            visited[nx][ny] += visited[cx][cy]

    return visited


print(BFS(0, 0)[N - 1][M - 1])
