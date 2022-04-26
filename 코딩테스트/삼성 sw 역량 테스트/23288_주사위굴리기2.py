from collections import deque

# 23288 주사위 굴리기 2
# 세로크기, 가로크기, 이동 횟수 K
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
ans = 0  # 각 이동에서 획득하는 점수의 합

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [2, 4, 1, 3, 5, 6]


def changeDice(dir):
    if dir == 0:  # 동쪽 이동
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    if dir == 1:  # 남쪽 이동
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    if dir == 2:  # 서쪽 이동
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    if dir == 3:  # 북쪽 이동
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]


d = 0
dice_bottom = 6
nx, ny = 0, 0
dice_x, dice_y = 0, 0


# 주사위 굴러가서 도착하는 함수
def diceTumble():
    global d, nx, ny, dice_x, dice_y
    dice_x, dice_y = nx, ny
    nx = dice_x + dx[d]
    ny = dice_y + dy[d]
    if not (0 <= nx < N and 0 <= ny < M):
        d = (d + 2) % 4
        nx, ny = dice_x + dx[d], dice_y + dy[d]
    changeDice(d)
    point = pointBFS(nx, ny)
    if dice[5] > board[nx][ny]:
        d = (d + 1) % 4
    elif dice[5] < board[nx][ny]:
        d = (d + 3) % 4
    return point


# 도착칸에 대한 점수 합산 BFS
def pointBFS(px, py):
    visited = [[0] * M for _ in range(N)]
    x, y = px, py
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    t = board[x][y]
    p = board[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and t == board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                p += board[nx][ny]
            else:
                continue
    return p


# 주사위 이동횟수만큼 반복
for i in range(K):
    ans += diceTumble()

# 최종 점수
print(ans)
