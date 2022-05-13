# 11478 서로 다른 부분 문자열의 개수
S = input()
answer = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        temp=S[i:j + 1]
        answer.add(temp)
print(len(answer))
