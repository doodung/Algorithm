#7576 토마토
from collections import deque

def bfs():
    while queue:    
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<N and -1<ny<M and board[nx][ny]==0:
                board[nx][ny]=board[x][y]+1
                queue.append((nx,ny))


def result():
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                return print(-1)
            answer = max(answer,board[i][j])
    return print(answer-1)
    

M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            queue.append((i,j))

bfs()
result()
