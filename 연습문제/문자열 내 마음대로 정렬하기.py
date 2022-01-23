def solution(a, b):
    answer = 0
    if(a>b):
        temp=a
        a=b
        b=temp

    return sum(range(a,b+1))