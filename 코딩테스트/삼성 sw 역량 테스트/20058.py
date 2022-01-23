# 20058 얼음

import sys
sys.setrecursionlimit(10 ** 5)
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, q = map(int, input().split())
n = 2 ** n
ice = [list(map(int, input().split())) for _ in range(n)]

for L in list(map(int, input().split())):
    # 회전
    k = 2 ** L
    for x in range(0, n, k):
        for y in range(0, n, k):
            tmp = [ice[i][y:y + k] for i in range(x, x + k)]
            for i in range(k):
                for j in range(k):
                    ice[x + j][y + k - 1 - i] = tmp[i][j]

    # 인접한 얼음 카운팅
    cnt = [[0] * n for i in range(n)]
    for x in range(0, n):
        for y in range(0, n):
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and ice[nx][ny]:
                    cnt[x][y] += 1

    # 얼음 제거
    for x in range(0, n):
        for y in range(0, n):
            if ice[x][y] > 0 and cnt[x][y] < 3:
                ice[x][y] -= 1

# 남아있는 얼음의 합
print(sum(sum(i) for i in ice))

# (x,y)가 속한 덩어리의 크기
def dfs(x, y):
    ret = 1
    ice[x][y] = 0
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and ice[nx][ny]:
            ret += dfs(nx, ny)
    return ret

# 제일 큰 덩어리
ans = 0
for x in range(n):
    for y in range(n):
        if ice[x][y] > 0:
            ans = max(ans, dfs(x, y))
print(ans)