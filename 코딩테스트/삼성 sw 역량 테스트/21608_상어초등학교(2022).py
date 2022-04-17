# 21608 상어초등학교
# 2022-03-31 doodung

N = int(input())
board = [[0] * N for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
like, like_list = [], []
answer = 0

for i in range(N * N):
    stu = list(map(int, input().split()))
    like = stu[1:]
    like_list.append(stu)
    temp = []

    # 맨 처음 student는 무조건 가운데 위치.
    if i == 0:
        board[1][1] = stu[0]
        continue

    for j in range(N):
        for k in range(N):
            sum_like, empty = 0, 0
            if board[j][k] != 0:
                continue
            for l in range(4):
                nx = j + dx[l]
                ny = k + dy[l]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] in like:
                        sum_like += 1
                    if board[nx][ny] == 0:
                        empty += 1
            temp.append((sum_like, empty, (j, k)))
    temp.sort(key=lambda x: (-x[0], -x[1], x[2]))
    board[temp[0][2][0]][temp[0][2][1]] = stu[0]

like_list.sort()
for i in range(N):
    for j in range(N):
        sat = 0
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in like_list[board[i][j] - 1]:
                    sat += 1
        if sat != 0:
            answer += (10 ** (sat - 1))
print(answer)
