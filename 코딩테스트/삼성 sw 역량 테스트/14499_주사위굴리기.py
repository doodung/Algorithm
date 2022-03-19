# 14499 주사위 굴리기
# 2022-03-20 doodung

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
move = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
nx, ny = x, y


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동 1 서 2 북 3 남 4
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


for dir in move:
    nx += dx[dir - 1]
    ny += dy[dir - 1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[dir - 1]
        ny -= dy[dir - 1]
        continue
    turn(dir)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])
