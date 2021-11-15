# 17779
# 게리맨더링2

N = int(input())
board = [[0 for _ in range(N + 1)]]
total = 0

for i in range(N):
    data = [0] + list(map(int, input().split()))
    total += sum(data)  # 총 인구수
    board.append(data)
min_diff = int(1e9)


def solve(x, y, d1, d2):
    global min_diff
    gu = [[0] * (N + 1) for _ in range(N + 1)]
    people = [0, 0, 0, 0, 0]
    # 경계선 그리기
    gu[x][y] = 5
    for i in range(1, d1 + 1):
        gu[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        gu[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        gu[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        gu[x + d2 + i][y + d2 - i] = 5

    # 1번 선거구
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if gu[i][j] == 5:  # 경계 만나면 break
                break
            else:
                people[0] += board[i][j]  # 인구수 더하기

    # 2번 선거구
    for i in range(1, x + d2 + 1):
        for j in range(N, y, -1):
            if gu[i][j] == 5:
                break
            else:
                people[1] += board[i][j]

    # 3번 선거구
    for i in range(x + d1, N + 1):
        for j in range(1, y - d1 + d2):
            if gu[i][j] == 5:
                break
            else:
                people[2] += board[i][j]

    # 4번 선거구
    for i in range(x + d2 + 1, N + 1):
        for j in range(N, y - d1 + d2 - 1, -1):
            if gu[i][j] == 5:
                break
            else:
                people[3] += board[i][j]

    # 5번 선거구는 전체에서 나머지 뺀 값
    people[4] = total - sum(people[0:4])

    # 최소 인구수의 차이 갱신하며 구함
    min_diff = min(min_diff, max(people) - min(people))


for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 > N:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > N:
                    continue
                solve(x, y, d1, d2)

print(min_diff)
