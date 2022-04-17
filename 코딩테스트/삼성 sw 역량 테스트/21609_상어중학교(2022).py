from collections import deque

# 21609 상어중학교
# 2022-03-31 doodung

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
count = 0


# 블록 그룹 찾기
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[x, y]], []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 일반블럭
                if board[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    block_cnt += 1
                    blocks.append([nx, ny])
                # 무지개 블럭
                elif board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append([nx, ny])

    for x, y in rainbows:
        visited[x][y] = 0
    # 블럭 총 갯수, 무지개 갯수, 방문한 곳 좌표
    return [block_cnt, rainbow_cnt, blocks + rainbows]


# 중력
def gravity(board):
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] > -1:
                g = i
                while True:
                    if 0 <= g + 1 < N and board[g + 1][j] == -2:
                        board[g + 1][j] = board[g][j]
                        board[g][j] = -2
                        g += 1
                    else:
                        break


while 1:
    visited = [[0] * N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_join = bfs(i, j, board[i][j])
                if block_join[0] >= 2:
                    blocks.append(block_join)

    blocks.sort(reverse=True)

    # 블록 제거
    if not blocks:
        break

    for x, y in blocks[0][2]:
        board[x][y] = -2
    count += blocks[0][0] ** 2

    gravity(board)

    # 90도 반시계 회전
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - 1 - j][i] = board[i][j]

    gravity(new_board)
    board = new_board

print(count)
