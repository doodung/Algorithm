def solution(s):
    answer = 10000
    for i in range(1,len(s)//2+2):
        res=''
        cnt=1
        temp=s[:i]
        for j in range(i,len(s)+i,i):
            if temp==s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    res+=temp
                else:
                    res+=str(cnt)+temp
                temp=s[j:j+i]
                cnt=1
        answer=min(answer,len(res))
    return answer