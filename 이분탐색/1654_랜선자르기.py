# 1654 랜선자르기
K, N = map(int, input().split())
Lan = []
for i in range(K):
    Lan.append(int(input()))
start = 1
end = max(Lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in Lan:
        cnt += (l // mid)
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
