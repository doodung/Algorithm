from collections import deque

# 20057 마법사 상어와 토네이도
# 2022-04-01 doodung

N = int(input())
board = [list(map(int, input().split(' '))) for i in range(N)]
ton = 0
rate = [[0, 0, 0.05, 0, 0],
        [0, 0.1, 0, 0.1, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0]]

# 왼 아래 오른쪽 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x, y = N // 2, N // 2
dir = 0
l = 0
dist = 1
max_fish = 0


def sand(x, y, rate, board):
    s = board[x][y]
    move = 0  # 흩날린 모래양
    inner = 0  # 격자 안에 흩날린 모래양
    for i in range(5):
        for j in range(5):
            if rate[i][j] == 0:
                continue
            nx, ny = x - 2 + i, y - 2 + j
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += int(s * rate[i][j])
                inner += int(s * rate[i][j])
            move += int(s * rate[i][j])
    return [move, inner]


# 모래 회전 (왼쪽 90도)
def rotate(rate):
    temp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[N - 1 - j][i] = rate[i][j]
    return temp


visited = [[0] * N for _ in range(N)]
# 토네이도 위치
while True:
    s = board[x][y]
    get = sand(x, y, rate, board)
    visited[x][y] = 1  # 방문 체크
    alpha = s - get[0]  # 흩날리고 남은 모래 (알파)

    # 알파가 격자 안에 있으면 board를 업로드
    ax, ay = x + dx[d], y + dy[d]
    if 0 <= ax and ax < n and 0 <= ay and ay < n:
        board[ax][ay] += alpha
        get[1] += alpha  # 격자 내 날린 모래에 추가

    board[locx][locy] = 0  # 현재 위치 모래 0

    result += sand - get[1]  # 바깥으로 날린 모래


    for d in range(4):
        tx = dx[d]
        ty = dy[d]
        print(x, y)
        for i in range(dist):
            nx = x + tx
            ny = y + ty
            if nx == 0 and ny == 0:
                exit(0)

            x, y = nx, ny

        if d == 1 or d == 3:
            dist += 1
            rate = rotate(rate)
