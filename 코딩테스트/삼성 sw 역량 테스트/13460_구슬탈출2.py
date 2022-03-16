from collections import deque

# 13460 구슬탈출2
# 2022-03-16 doodung

N, M = map(int, input().split())
board = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rx, ry = 0, 0
bx, by = 0, 0
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

        if count > 10:
            continue

        for k in range(4):
            rnx, rny, r_move = move(r_x, r_y, dx[k], dy[k])
            bnx, bny, b_move = move(b_x, b_y, dx[k], dy[k])

            if board[bnx + dx[k]][bny + dy[k]] == 'O':
                continue

            if board[rnx + dx[k]][rny + dy[k]] == 'O' and count < 10:
                return count + 1

            if rnx == bnx and rny == bny:
                if r_move > b_move:
                    rnx -= dx[k]
                    rny -= dy[k]
                else:
                    bnx -= dx[k]
                    bny -= dy[k]

            if r_x == rnx and r_y == rny and b_x == bnx and b_y == bny:
                continue

            q.append((rnx, rny, bnx, bny, count + 1))

    return -1


result = bfs()
print(result)
