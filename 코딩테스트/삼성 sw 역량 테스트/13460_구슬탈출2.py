from collections import deque

# 13460 구슬탈출2
# 2022-03-16 doodung

N, M = map(int, input().split())
board = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rx, ry = 0, 0
bx, by = 0, 0

# 빨간 공과 파란공 위치 체크
for i in range(N):
    board.append(list(input().strip()))
    for j in range(len(board[i])):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j


def move(x, y, dx, dy):
    nx, ny = x, y
    moving = 0
    while True:
        # 장애물 또는 벽이 아니고, 구멍도 아닐때 이동
        if board[nx + dx][ny + dy] != '#' and board[nx + dx][ny + dy] != 'O':
            nx += dx
            ny += dy
            moving += 1
        else:
            break
    return nx, ny, moving


def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 0))
    while q:
        r_x, r_y, b_x, b_y, count = q.popleft()

        # 10번을 넘으면 -1 출력
        if count > 10:
            continue

        for k in range(4):
            rnx, rny, r_move = move(r_x, r_y, dx[k], dy[k])
            bnx, bny, b_move = move(b_x, b_y, dx[k], dy[k])

            # 파란색이 구멍 빠지면 실패
            if board[bnx + dx[k]][bny + dy[k]] == 'O':
                continue

            # 10번 이내이고, 빨간색이 구멍에 빠지면 성공
            if board[rnx + dx[k]][rny + dy[k]] == 'O' and count < 10:
                return count + 1

            # 빨간색과 파란색이 같은 칸에 있으면
            if rnx == bnx and rny == bny:
                # 이동거리가 더 많은 구슬 == 더 늦게 이동한 구슬이므로 한칸 뒤로
                if r_move > b_move:
                    rnx -= dx[k]
                    rny -= dy[k]
                else:
                    bnx -= dx[k]
                    bny -= dy[k]

            # 방문 여부 확인
            if r_x == rnx and r_y == rny and b_x == bnx and b_y == bny:
                continue

            # 방문하지 않았다면 새로 큐에 추가 후 방문처리
            q.append((rnx, rny, bnx, bny, count + 1))

    return -1


result = bfs()
print(result)
