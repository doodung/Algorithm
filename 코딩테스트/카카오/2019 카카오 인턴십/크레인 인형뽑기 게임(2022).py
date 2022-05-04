def solution(board, moves):
    get = []
    N=len(board)
    cnt=0
    for m in moves:
        for i in range(N):
            if board[i][m-1]==0:
                continue
            else:
                if len(get)<1 or (len(get)>=1 and get[-1]!=board[i][m-1]):
                    get.append(board[i][m-1])
                    board[i][m-1] = 0
                if len(get)>=1 and get[-1]==board[i][m-1]:
                    get.pop()
                    cnt+=1
                    board[i][m-1] = 0
                break
    return cnt*2