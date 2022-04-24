from itertools import combinations

# 15686 치킨배달
# pypy : 184 python : 784
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i, j))
        if board[i][j] == 1:
            home.append((i, j))

answer = 999999
for c in combinations(chicken, M):
    cnt = 0
    for h in home:
        mini = 100
        for i in range(M):
            mini = min(mini, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        cnt += mini
    answer = min(answer, cnt)
print(answer)
