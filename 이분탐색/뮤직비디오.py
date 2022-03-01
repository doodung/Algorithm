import sys

# 뮤직비디오(결정 알고리즘)
sys.stdin = open("input.txt", "r")


def Count(capacity):
    cnt = 1
    s = 0
    for x in music:
        if s + x > capacity:
            cnt += 1
            s = x
        else:
            s += x
    return cnt


n, m = map(int, input().split())
music = list(map(int, input().split()))
max_music = max(music)
lt = 1
rt = sum(music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_music and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
