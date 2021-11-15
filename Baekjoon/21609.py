# 21609 상어중학교
from collections import deque

# N -> 한변의 크기, M -> 색상의 개수
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = 0


# 인접 블록 찾기 -> 블록크기, 무지개크기, 블록좌표 리턴
# 검 : -1, 무지개 : 0
def bfs(x, y, color):
    # 왼쪽 상단부터 오른쪽으로
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append([x, y])

    block_cnt, rainbow_cnt = 1, 0  # 블록 개수, 무지개 블록 개수
    blocks, rainbows = [[x, y]], []  # 블록 좌표 넣을 리스트, 무지개 좌표 넣을 리스트


    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 안이면서 방문 안한 일반 블록인 경우
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            # 범위 안이면서 방문 안한 무지개 블록의 경우
            elif 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개 블록 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]


# 블록 제거 함수
def remove(block):
    for x, y in block:
        board[x][y] = -2


# 중력 함수
def gravity(board):
    for i in range(N - 2, -1, -1):  # 밑에서부터 체크
        for j in range(N):
            if board[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < N and board[r + 1][j] == -2:  # 다음 행이 인덱스 범위 안이면서 -2면 아래로 다운
                        board[r + 1][j] = board[r][j]
                        board[r][j] = -2
                        r += 1
                    else:
                        break


# 반시계 회전 함수
def rot90(board):
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N-1-j][i] = board[i][j]
    return new_board


# 1. 오토플레이 -> while(2.가장 크기 큰 블록 찾기,3. 블록제거 + 점수 더하기, 4. 중력, 5. 90회전 6. 중력)
while True:
    # 2. 크기 가장 큰 블록 찾기
    visited = [[0] * N for _ in range(N)]  # 방문체크
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:  # 일반 블록이면서 방문 안했으면
                visited[i][j] = 1  # 방문
                block_info = bfs(i, j, board[i][j])  # 인접한 블록 찾기
                # block_info = [블록크기, 무지개블록개수, 블록좌표]
                if block_info[0] >= 2:  # 블록 크기가 2보다 크면
                    blocks.append(block_info)  # 배열에 append
    blocks.sort(reverse=True)

    # 3. 블록 제거 + 점수 더하기
    if not blocks:
        break
    remove(blocks[0][2])  # 블록 제거
    score += blocks[0][0]**2  # 점수 더하기

    # 4. 중력
    gravity(board)

    # 5. 90 회전
    board = rot90(board)

    # 6. 중력
    gravity(board)

print(score)
