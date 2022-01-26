# 1697
# 숨바꼭질
from collections import deque

def bfs():
    global N,K
    queue=deque()
    queue.append(N)
    while queue:
        x=queue.popleft()
        
        if x == K :
            print(board[x])
            break
        
        for nx in(x-1,x+1,x*2):
            if 0 <= nx <=Max and not board[nx]:
                board[nx] = board[x]+1
                queue.append(nx)
                
N ,K = map(int,input().split())
Max = 10**5
board= [0]*(Max+1)

bfs()
