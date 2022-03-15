# 13458 시험감독
# 2022-03-15 doodung

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
manager, assi = 0, 0

for i in range(N):
    A[i] -= B
    manager += 1
    if A[i] >= 0:
        assi += A[i] // C
        if A[i] % C != 0:
            assi += 1

print(manager + assi)
