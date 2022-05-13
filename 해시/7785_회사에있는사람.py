# 7785 회사에 있는 사람
n = int(input())
company = {}
temp = []
for _ in range(n):
    name, status = map(str, input().split())
    if name in company.keys():
        temp = [company[name], status]
        company[name] = temp
    else:
        company[name] = status
answer = []
cnt = 0
for name, status in company.items():
    if status == 'enter' or status[-1] == 'enter':
        answer.append(name)
answer.sort(reverse=True)
set(answer)
for a in answer:
    print(a)
