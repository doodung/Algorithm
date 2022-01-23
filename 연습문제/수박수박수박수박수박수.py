def solution(seoul):
    answer = ''
    index=0
    for i in range(len(seoul)):
        if (seoul[i]=="Kim") :
            index=i
    answer="김서방은 %d에 있다" %(index)
    return answer