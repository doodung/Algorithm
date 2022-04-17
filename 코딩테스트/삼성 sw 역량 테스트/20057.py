### 백준 #20057
### 마법사 상어와 토네이도

from sys import stdin


def update(x, y, board, rate):
    sand = board[x][y]  # 현재 위치 모래양
    move = 0  # 흩날린 모래양
    inner = 0  # 격자 안에 흩날린 모래양

    for i in range(5):
        for j in range(5):
            if rate[i][j] == 0:
                continue
            nx, ny = x - 2 + i, y - 2 + j
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += int(sand * rate[i][j])
                inner += int(sand * rate[i][j])
            move += int(sand * rate[i][j])
    return [move, inner]


def turn(rate):
    temp = [[0 for x in range(5)] for y in range(5)]

    for i in range(5):
        for j in range(5):
            temp[5 - j - 1][i] = rate[i][j]

    return temp


# 1. n 입력
n = int(stdin.readline())

# 2. 모래밭 정보
global board
board = []

for i in range(n):
    board.append(list(map(int, stdin.readline().split(' '))))

# 3. 현재 토네이도 위치
locx = n // 2
locy = n // 2

# 4. 방향벡터(시계방향) : 왼,아래,오른,위
d = 0  # 현재 방향
nd = 0  # 다음 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 5. 모래 변화 비율
rate = [[0, 0, 0.05, 0, 0],
        [0, 0.1, 0, 0.1, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0]]

#
check = [[0 for i in range(n)] for j in range(n)]
result = 0

while True:
    # 흩날리는 모래 업데이트
    sand = board[locx][locy]
    get = update(locx, locy, board, rate)
    check[locx][locy] = 1  # 방문 체크
    alpha = sand - get[0]  # 흩날리고 남은 모래 (알파)

    # 알파가 격자 안에 있으면 board를 업로드
    ax, ay = locx + dx[d], locy + dy[d]
    if 0 <= ax < n and 0 <= ay < n:
        board[ax][ay] += alpha
        get[1] += alpha  # 격자 내 날린 모래에 추가

    board[locx][locy] = 0  # 현재 위치 모래 0

    result += sand - get[1]  # 바깥으로 날린 모래

    # (0,0) 위치면 종료
    if locx == 0 and locy == 0:
        break

    # 회전 가능하면 다음 이동방향 바꾸기
    newx, newy = locx + dx[nd], locy + dy[nd]
    if check[newx][newy] == 0:
        d = nd
        nd += 1
        rate = turn(rate)

        if nd == 4:
            nd = 0

    locx, locy = locx + dx[d], locy + dy[d]

print(result)
