from collections import deque

# 3190 뱀
# 2022-03-20 doodung

N = int(input())
K = int(input())
# 보드를 모두 0으로 채움. 사과는 2로 채우고, 뱀은 1로 채울 것
board = [[0] * N for _ in range(N)]

#  사과의 위치
for i in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 2

L = int(input())
dic = dict()

# X초가 끝난 후 C 방향으로 회전. 딕셔너리 사용해 시간을 키값으로, 방향을 밸류로
for j in range(L):
    X, C = input().split()
    dic[int(X)] = C

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
snake = deque()
snake.append((0, 0))
x, y = 0, 0
# 초기값 오른쪽
direction = 0


# 뱀이 이동할때 머리와 꼬리 한칸씩 전진 (몸의 길이 그대로)
# 사과를 먹으면 머리는 전진, 꼬리는 그대로 (몸의 길이 한칸 늘어남)
# -> 큐에서 pop 하지 않고 큐에 현재 머리 위치만 push해서 몸 길이 늘려줌
def turn(d):
    global direction
    # 우(0), 하(1), 좌(2), 상(3)
    # 왼쪽 회전
    if d == 'L':
        direction = (direction - 1) % 4
    # 오른쪽 회전
    else:
        direction = (direction + 1) % 4


while 1:
    time += 1
    x += dx[direction]
    y += dy[direction]

    # 종료조건 : 뱀이 벽에 부딪히면 종료
    if x < 0 or x >= N or y < 0 or y >= N:
        break

    # 뱀이 이동한 칸에 사과가 있으면
    if board[x][y] == 2:
        board[x][y] = 1
        snake.append((x, y))
        # 해당 time이 딕셔너리에 존재하면 방향 변경해줌
        if time in dic:
            turn(dic[time])

    # 뱀이 이동한 칸에 사과가 없으면
    elif board[x][y] == 0:
        board[x][y] = 1
        snake.append((x, y))
        # 꼬리부분 자름
        nx, ny = snake.popleft()
        board[nx][ny] = 0
        if time in dic:
            turn(dic[time])

    # 종료조건 : 뱀이 자기 자신의 몸과 부딪히면 종료
    else:
        break

print(time)
