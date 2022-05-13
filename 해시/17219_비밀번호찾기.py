# 17219 비밀번호찾기
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, pas = map(str, input().split())
    dic[site] = pas

answer=[]
for _ in range(M):
    site = input()
    answer.append(dic[site])

for a in range(M):
    print(answer[a])
