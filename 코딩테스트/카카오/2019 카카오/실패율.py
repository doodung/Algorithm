def solution(N, stages):
    fail = {}
    people = len(stages)
    for i in range(1,N+1):
        if people != 0:
            count = stages.count(i)
            fail[i] = count/people
            people -= count
        else:
            fail[i]=0

    return sorted(fail,key=lambda x:fail[x], reverse=True)