# 14499 주사위 굴리기
# 2022-03-20 doodung

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
move = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 가장 처음 주사위값은 0
# 윗면, 동쪽, 서쪽, 북쪽, 남쪽, 바닥면 순
dice = [0, 0, 0, 0, 0, 0]


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 회전 : 동 1 서 2 북 3 남 4
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


for dir in move:
    # 움직이는 nx,ny 좌표를 구함
    x += dx[dir - 1]
    y += dy[dir - 1]
    # 맵보다 커지지 않도록
    if x < 0 or x >= N or y < 0 or y >= M:
        # 원래 값으로 복구
        x -= dx[dir - 1]
        y -= dy[dir - 1]
        continue
    turn(dir)
    # 칸이 0 이라면 주사위 바닥면을 복사
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    # 지도 칸에 값이 있다면 바닥에 칸의 값을 넣고, 칸은 0으로
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    # 결과 : 상단에 쓰여 있는 값
    print(dice[0])
