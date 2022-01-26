# 4179 불!
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

R ,C = map(int,input().split())
board=[list(input().strip()) for _ in range(R)]
cnt=0
F,J=deque(),deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            J.append((i,j))
        if board[i][j] == 'F':
            F.append((i,j))


def bfs():
    global F,J,cnt
    
    while 1:
        cnt+=1
        temp=[]
        
        while F:
            x,y = F.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<R and 0<=ny<C:
                    if board[nx][ny] == '.' or board[nx][ny]=='$':
                        temp.append((nx,ny))
                        board[nx][ny] = 'F'
                        
        F=deque(temp)
        temp=[]
        
        while J:
            x,y = J.popleft()
            
            if x == 0 or y == 0 or x == R-1 or y == C-1:
                return cnt
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<R and 0<=ny<C and board[nx][ny]=='.':
                        board[nx][ny]='J'
                        board[x][y]='$'
                        temp.append((nx,ny))
                        
        J=deque(temp)
        
        if not J :
            return False

if bfs():
    print(cnt)
else:
    print('IMPOSSIBLE')
        
                
    
