# 마법사 상어와 비바라기 - BOJ 21610
# 구현
N, M = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

move = []
for i in range(M):
    tmp = list(map(int, input().split()))
    move.append([tmp[0] - 1, tmp[1]])
    # dx, dy는 0부터 시작하므로 -1 해줘야함

for k in range(M):
    next_clouds = []
    # step1 구름 이동 : %N을 해서 범위 넘어서도 가능하게 해야함
    for cloud in clouds:
        nx = (N + cloud[0] + dx[move[k][0]] * move[k][1]) % N
        ny = (N + cloud[1] + dy[move[k][0]] * move[k][1]) % N
        next_clouds.append([nx, ny])
    visited = [[False] * N for _ in range(N)]

    # step2 비가 내려 물의 양 1 증가
    for cloud in next_clouds:
        water[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True

    # step3 구름 사라짐
    clouds = []

    # 대각선 방향
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        count = 0
        for i in range(4):
            nx = cloud[0] + cx[i]
            ny = cloud[1] + cy[i]
            # step4 물복사버그 마법 : 대각선 방향에 물이 있는 바구니 수만큼 바구니 물 양 증가
            if 0 <= nx < N and 0 <= ny < N and water[nx][ny] >= 1:
                count += 1
        water[cloud[0]][cloud[1]] += count

    # step5 물의양2 이상인 모든 칸에 구름 생기고 -> 물의 양 2 줄어든다
    for i in range(N):
        for j in range(N):
            if water[i][j] >= 2 and visited[i][j] == False:
                water[i][j] -= 2
                clouds.append([i, j])

    ans = 0
    for i in range(N):
        ans += sum(water[i])

print(ans)
