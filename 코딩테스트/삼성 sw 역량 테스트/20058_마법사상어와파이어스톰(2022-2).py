from collections import deque

N, Q = map(int, input().split())
I = 2 ** N
board = [list(map(int, input().split())) for _ in range(I)]
L = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# 부분 격자로 나눈 후, 모든 부분 격자를 시계방향으로 90도 회전
def makeGrid(l):
    temp = [[0] * I for _ in range(I)]
    L2 = 2 ** l
    # 큰 사각형
    for i in range(0, I, L2):
        for j in range(0, I, L2):
            for li in range(0, L2):
                for lj in range(0, L2):
                    temp[i + lj][j + (L2 - 1) - li] = board[i + li][j + lj]
    return temp


def makeWater():
    ice = []
    for i in range(I):
        for j in range(I):
            cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < I and 0 <= ny < I and board[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                ice.append((i, j))

    for x, y in ice:
        if board[x][y] > 0:
            board[x][y] -= 1


def iceBFS(x, y):
    q = deque()
    ice = 1
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                if board[nx][ny] > 0:
                    ice += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return ice


# 파이어스톰 총 Q번 시전
for l in range(Q):
    board = makeGrid(L[l])
    makeWater()

max_ice = []
ans = 0
visited = [[False] * I for _ in range(I)]
for i in range(I):
    for j in range(I):
        if not visited[i][j] and board[i][j] > 0:
            visited[i][j] = True
            ans = max(ans, iceBFS(i, j))

# 결과
# 남아있는 얼음의 합
# 가장 큰 덩어리가 차지하는 칸의 개수, 덩어리가 없으면 0
print(sum(sum(board, [])))
print(ans)
