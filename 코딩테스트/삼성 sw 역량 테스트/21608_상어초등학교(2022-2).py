# 상어초등학교

N = int(input())
# 학생 번호, 좋아하는 학생 번호 4개
student = [list(map(int, input().split())) for i in range(N ** 2)]
ans = []
board = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for s in range(len(student)):
    if s == 0:
        stu = student[0][0]
        board[1][1] = stu
        continue
    stu = student[s][0]
    like_student = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                like, blank = 0, 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in student[s][1:]:
                            like += 1
                        if board[nx][ny] == 0:
                            blank += 1
                like_student.append((like, blank, i, j))
    like_student.sort(key=lambda x: (-x[0], -x[1]))
    s_like, s_blank, sx, sy = like_student[0]
    board[sx][sy] = stu

t = 0
cnt = 0
l = []
#   answer= 학생 만족도 : 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수가 n일때 10**n
for x in range(N):
    for y in range(N):
        t = board[x][y]
        for i in range(len(student)):
            if student[i][0] == t:
                l = student[i][1:]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in l:
                    cnt += 1
        if cnt == 0:
            ans.append(0)
        else:
            ans.append(10 ** (cnt - 1))
        cnt = 0
print(sum(ans))
