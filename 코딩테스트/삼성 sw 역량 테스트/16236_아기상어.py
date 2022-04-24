from collections import deque
# 16236 아기상어
# pypy 244 python 284

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
fish = [list(map(int, input().split())) for i in range(N)]
sharkX, sharkY = 0, 0
for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            sharkX = i
            sharkY = j
            fish[i][j] = 0
            break


def bfs(x, y, size):
    q = deque()
    dist = 0
    q.append((x, y, dist))
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    eatFish = []
    while q:
        x, y, dist = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if fish[nx][ny] <= size:
                    q.append((nx, ny, dist+1))
                    if 0 < fish[nx][ny] < size:
                        eatFish.append((nx, ny, dist+1))
                visited[nx][ny] = 1

    return sorted(eatFish, key=lambda c: (-c[2], -c[0], -c[1]))


eat = 0
shark_size = 2
time = 0

while 1:
    shark = bfs(sharkX, sharkY, shark_size)
    if len(shark) == 0:
        break
    sx, sy, dis = shark.pop()
    time += dis
    fish[sharkX][sharkY], fish[sx][sy] = 0, 0
    sharkX, sharkY = sx, sy
    eat += 1
    if eat == shark_size:
        shark_size += 1
        eat = 0

print(time)
