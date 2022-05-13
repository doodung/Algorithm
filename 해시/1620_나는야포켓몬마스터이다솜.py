# 1620 나는야포켓몬마스터이다솜
# 키,밸류 밸류,키 두개로 딕셔너리 만들어야지
# 탐색할때 시간초과 안남요
N, M = map(int, input().split())
pocket_name = {}
pocket_num = {}
for n in range(N):
    name = str(input())
    pocket_name[n + 1] = name
    pocket_num[name] = n + 1
answer = []
for _ in range(M):
    num = str(input())
    if num.isdigit():
        num = int(num)
        answer.append(pocket_name[num])
    else:
        answer.append(pocket_num[num])

for a in answer:
    print(a)
