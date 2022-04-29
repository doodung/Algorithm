# 19237 어른상어
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 0은 빈칸

priority = []
temp = []

# 각 상어의 방향
shark_dir = list(map(lambda x: int(x) - 1, input().split()))
# 0,1,2,3 -> 위,아래,왼쪽,오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for i in range(M):
    for j in range(4):
        temp.append(list(map(lambda x: int(x) - 1, input().split())))
    priority.append(temp)
    temp = []

smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
for _ in range(1000):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if board[i][j] != 0:
                smell[i][j] = [board[i][j], K]

    # 2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 냄새 뿌림
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                flag = False
                shark_num = board[i][j]
                # dir -> 현재 보고 있는 위치
                dir = shark_dir[shark_num - 1]
                # next_dir -> 상어가 다음에 갈 위치
                next_dir = priority[shark_num - 1][dir]
                for d in next_dir:  # 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡음
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][1] == 0:
                            shark_dir[shark_num-1]=d
                            if new_board[nx][ny] == 0:
                                new_board[nx][ny] = shark_num
                            else:
                                new_board[nx][ny] = min(new_board[nx][ny], shark_num)
                            flag = True
                            break
                if flag:
                    continue

                for dd in next_dir:
                    nx = i + dx[dd]
                    ny = j + dy[dd]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == shark_num:
                            shark_dir[shark_num - 1] = dd
                            new_board[nx][ny] = shark_num
                            break

    board = new_board
    ans += 1
    if sum(sum(board[s]) for s in range(N)) == 1:
        print(ans)
        break

# 1번 상어만 격자에 남게 되기까지 걸리는 시간 출력
# 1000초가 넘어도 다른 상어가 격자에 남아있으면 -1 출력
else:
    print(-1)
