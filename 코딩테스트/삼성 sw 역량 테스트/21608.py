# 상어초등학교 - BOJ 21608
# 구현
import sys

n = int(sys.stdin.readline())
student = n * n
classroom = [[0] * n for _ in range(n)]
like_friends = [[] for _ in range(student + 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(student):
    student_array = list(map(int, input().split()))
    like = student_array[1:]
    like_friends[student_array[0]] = like

    # 맨 처음 student는 무조건 가운데 위치.
    if student == 0:
        classroom[1][1] = student_array[0]
        continue

    temp = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0, 0
            # 이미 그 자리에 학생이 있으면 continue
            if classroom[i][j] != 0:
                continue
            # 상하좌우 체크
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 범위 넘어가면 continue
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                    continue
                # classroom 상하좌우 중 좋아하는 학생이 있으면
                if classroom[nx][ny] in like:
                    sum_like += 1
                # classroom 상화좌우 중 비어 있으면
                if classroom[nx][ny] == 0:
                    sum_empty += 1
            # sum_like, sum_empty, (i,j => 해당 행,열값) append
            temp.append((sum_like, sum_empty, (i, j)))

    # 모든 행과 열(n*n) 범위 살핀 후,
    # temp 리스트를 sort 해줘서 조건에 맞게 sum_like 값이 많은 때, -> -x[0]
    # 그 후 sum_like 값이 동일하다면 sum_empty 값이 많은 때, -> -x[1]
    # 또한 sum_empty 값도 동일하다면 행 값이 작을 때,
    # 행 값도 동일하다면 열 값이 작을 때 순으로 정렬 -> x[2]
    temp.sort(key=lambda x: (-x[0], -x[1], x[2]))
    # 정렬 후 가장 첫 번째 있는 값의 행, 열값을 최적 위치로 선정하기 위하여 classroom 리스트의 해당 행, 열에 학생 번호로 변경
    # temp[0][2][0] -> 행, temp[0][2][1] -> 열
    classroom[temp[0][2][0]][temp[0][2][1]] = student_array[0]


# 마지막으로  classroom에 최적 자리로 선정된 학생들 하나하나
# 인접 지역에 얼마나 좋아하는 학생이 배치되었는지 확인하여 학생의 만족도를 계산
sum_answer = 0
for i in range(n):
    for j in range(n):
        answer = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if classroom[nx][ny] in like_friends[classroom[i][j]]:
                answer += 1
                continue
        if answer != 0:
            sum_answer += (10 ** (answer - 1))

print(sum_answer)