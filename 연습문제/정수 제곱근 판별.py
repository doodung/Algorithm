import math
def solution(n):
    answer = math.sqrt(n)
    if(answer%1==0):
        answer=(answer+1)**2
    else:
        answer=-1
    return int(answer)