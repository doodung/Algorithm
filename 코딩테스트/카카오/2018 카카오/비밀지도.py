def make_board(n,arr):
    board=[]
    for i in range(n):
        temp=bin(arr[i])[2:]
        if len(temp)<n:
            zero = (n-len(temp))*'0'
            board.append(zero+temp)
        else:
            board.append(temp)
    return board

def solution(n, arr1, arr2):
    answer = []
    board1=make_board(n,arr1)
    board2=make_board(n,arr2)

    for i in range(n):
        ans=''
        for j in range(n):
            if board1[i][j]=='1' or board2[i][j]=='1':
                ans+='#'
            if board1[i][j]=='0' and board2[i][j]=='0':
                ans+=' '
        answer.append(ans)

    return answer

