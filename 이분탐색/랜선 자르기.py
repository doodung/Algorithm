import sys

# 랜선 자르기(결정 알고리즘)
sys.stdin = open("input.txt", "r")


def Count(len):
    cnt = 0
    for x in cm:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
cm = [int(input()) for i in range(k)]
large = max(cm)
lt = 1
rt = large

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
