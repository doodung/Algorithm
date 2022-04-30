# 21609 상어중학교
# 격자 한 변의 크기, 색상의 개수
import copy
from collections import deque

N, M = map(int, input().split())
# 검은색 -1, 무지개 0, 일반 1이상 M이하 자연수

board = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def blockBFS(x, y):
    start_x, start_y = x, y
    q = deque()
    normal = 0
    q.append((x, y))
    visited[x][y] = True
    color = board[x][y]
    blockXY = [[x, y]]
    rainbowXY = []
    rainbow = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 일반 블록
                if 1 <= board[nx][ny] <= M and board[nx][ny] == color:
                    visited[nx][ny] = True
                    normal += 1
                    q.append((nx, ny))
                    cnt += 1
                    blockXY.append([nx, ny])
                # 무지개 블록
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    rainbow += 1
                    q.append((nx, ny))
                    rainbowXY.append([nx, ny])
                    cnt += 1

    for rx, ry in rainbowXY:
        visited[rx][ry] = False

    return [cnt, rainbow, start_x, start_y, blockXY + rainbowXY]


# 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.
# 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
def gravity():
    for gx in range(N - 2, -1, -1):
        for gy in range(N):
            if board[gx][gy] > -1:
                g = gx
                while 1:
                    if 0 <= g + 1 < N and board[g + 1][gy] == -2:
                        board[g + 1][gy] = board[g][gy]
                        board[g][gy] = -2
                        g += 1
                    else:
                        break

point = 0

def rotate():
    rotate_board = [[0] * N for _ in range(N)]
    for rx in range(N):
        for ry in range(N):
            rotate_board[N - 1 - ry][rx] = board[rx][ry]
    return rotate_board


while 1:
    block_group = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                bfs = blockBFS(i, j)
                if bfs[0] >= 2:
                    block_group.append(bfs)

    block_group.reverse()
    block_group.sort(key=lambda x: (-x[0], -x[1]))

    if not block_group:
        break

    for i in range(block_group[0][0]):
        for x, y in block_group[0][-1]:
            board[x][y] = -2

    # 점수 구하기
    point += block_group[0][0] ** 2

    # 중력 작용
    gravity()

    board = rotate()

    # 중력 작용
    gravity()


# 결과
# 획득한 점수의 합
print(point)
