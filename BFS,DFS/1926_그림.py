# 1926 그림
from collections import deque

def bfs(x,y):
    size = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                queue.append((nx,ny))
                board[nx][ny] = 0 
                size += 1
                
    return size

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for i in range(N) ]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j]=0
            answer.append(bfs(i,j))

print(len(answer))
print(max(answer) if answer else 0)

