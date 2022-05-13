# 9375 패션왕 신해빈
n = int(input())
answer = []
for _ in range(n):
    m = int(input())
    dic = {}
    for _ in range(m):
        name, category = map(str, input().split())
        if category in dic.keys():
            dic[category] += 1
        else:
            dic[category] = 1
    temp = 1
    for i in dic:
        temp *= (dic[i] + 1)
    print(temp - 1)
