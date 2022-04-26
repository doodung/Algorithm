# 21611 마법사 상어와 비바라기

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]
# info[i][0] -> di, info[i][1]-> si
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

# 왼쪽부터 ~ 대각선왼쪽아래까지
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
next_cloud = []

bdx = [-1, -1, 1, 1]
bdy = [-1, 1, 1, -1]


def waterMagic(x, y):
    cnt = 0
    for d in range(4):
        bnx = x + bdx[d]
        bny = y + bdy[d]
        if 0 <= bnx < N and 0 <= bny < N and board[bnx][bny] > 0:
            cnt += 1
    board[x][y] += cnt


for i in range(M):
    # 구름 이동
    for d in range(len(cloud)):
        dir = info[i][0] - 1
        nx = (N + cloud[d][0] + dx[dir] * info[i][1]) % N
        ny = (N + cloud[d][1] + dy[dir] * info[i][1]) % N
        next_cloud.append((nx, ny))

    # 구름 있는 칸에 비가 내림
    for cx, cy in next_cloud:
        board[cx][cy] += 1

    bug_dir = next_cloud
    cloud = []
    # 물이 증가한 칸 r,c에 물복사버그 마법 시전.
    for bx, by in bug_dir:
        waterMagic(bx, by)

    for j in range(N):
        for k in range(N):
            if board[j][k] >= 2 and (j, k) not in next_cloud:
                cloud.append((j, k))
                board[j][k] -= 2
    next_cloud = []

ans = 0
for i in range(N):
    for j in range(N):
        ans += board[i][j]


print(ans)
