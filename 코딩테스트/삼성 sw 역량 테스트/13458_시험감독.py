# 13458 시험감독
# 2022-03-15 doodung

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
# 총감독, 부감독
manager, assi = 0, 0

for i in range(N):
    # 총감독은 무조건 1명
    A[i] -= B
    manager += 1
    if A[i] >= 0:
        # 부감독은 한명당 C명 가능, 부감독은 1명 이상 가능
        assi += A[i] // C
        # 위의 계산 후에도 응시자수가 남아있을 수 있으므로 나머지가 0이 아니면 부감독 1명이 더필요함
        if A[i] % C != 0:
            assi += 1

print(manager + assi)
