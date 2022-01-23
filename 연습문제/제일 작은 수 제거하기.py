def solution(n):
    temp = str(n)
    answer=[]
    string=''
    for i in temp:
        answer+=[int(i)]
    answer.sort(reverse=True)
    for i in answer:
        string+=str(i)
    return int(string)