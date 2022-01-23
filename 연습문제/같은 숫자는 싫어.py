def solution(arr):
    answer = []
    j=0
    answer.append(arr[0])
    for i in range(0,len(arr)):
        if(answer[j]!=arr[i]):
            answer.append(arr[i])
            j=j+1
    return answer