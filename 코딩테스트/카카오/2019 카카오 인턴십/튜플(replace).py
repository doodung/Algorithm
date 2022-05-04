def solution(s):
    answer=[]
    s = s.replace("{" , "")
    s = s.replace("}","")
    s = s.split(",")

    dic = {}
    for i in s:
        if i in dic :
            dic[i] = dic[i]+1
        else:
            dic[i]=1

    data = sorted(dic.items(),key=lambda x:x[1] ,reverse =True)

    for i in data:
        answer.append(int(i[0]))

    return answer