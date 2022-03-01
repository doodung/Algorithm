def solution(n):
    answer = 0
    x=1
    for i in range(n,0,-1):
        if n%x == 1:
            answer=x
            break
        x+=1
    return answer