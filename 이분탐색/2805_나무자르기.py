# 2805 나무자르기
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for t in tree:
        if t >= mid:
            cnt += (t - mid)
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
