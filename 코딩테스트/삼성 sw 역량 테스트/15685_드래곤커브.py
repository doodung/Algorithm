# 15685 드래곤커브
# pypy3 120 python3 84

N = int(input())
dragon = [list(map(int, input().split())) for i in range(N)]
# dragon = [[x,y,시작방향,세대],..]]

dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 오, 위, 왼, 아

# 0세대 : 0
# 1세대 : 0 1
# 2세대 : 0 1 2 1
# 3세대 : 0 1 2 1 2 3 2 1
# 4세대 : 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1

dot = []
for i in range(N):
    q = []
    x, y, start, year = dragon[i]
    q.append(start)
    dot.append((x, y))
    for j in range(year):
        temp = []
        for k in range(len(q)):
            temp.append((q[-k - 1] + 1) % 4)
        q.extend(temp)

    for d in q:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        dot.append((nx, ny))
        x, y = nx, ny

dot = set(dot)
answer = 0
for gx, gy in dot:
    if (gx + 1, gy) in dot and (gx, gy - 1) in dot and (gx + 1, gy - 1) in dot:
        answer += 1
print(answer)
