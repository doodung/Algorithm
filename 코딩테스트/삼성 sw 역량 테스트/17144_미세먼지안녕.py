# 17144 미세먼지 안녕!
# pypy 384

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
air_up = 0
ux, uy = [0, -1, 0, 1], [1, 0, -1, 0]
wx, wy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(R):
    if board[i][0] == -1:
        air_up = i
        break


# 1. 미세먼지 확산
def dust():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                spread_q = board[i][j] // 5
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += spread_q
                        board[i][j] -= spread_q

    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]


# 2. 공기청정기 작동
def air(x, y, ddx, ddy):
    dir, t = 0, 0
    while 1:
        nx = x + ddx[dir]
        ny = y + ddy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue
        if board[nx][ny] == -1:
            break
        board[nx][ny], t = t, board[nx][ny]
        x, y = nx, ny


for i in range(T):
    dust()
    air(air_up, 0, ux, uy)
    air(air_up + 1, 0, wx, wy)

print(sum(sum(board[i]) for i in range(R)) + 2)
