def solution(n):
    answer = str(n)
    a=[]
    for i in range(len(answer)):
        a+=[int(answer[len(answer)-i-1:len(answer)-i])]
    return a