from copy import deepcopy

# 125836kb 196ms
board = [list(map(int, input().split())) for _ in range(4)]
dir = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
sea = []
max_fish = 0

# sea -> [[[물고기번호, 방향],[물고기번호, 방향]...]],[[물고기번호, 방향]...]]]
for i in range(4):
    temp = []
    for j in range(0, 8, 2):
        temp.append([board[i][j], board[i][j + 1] - 1])
    sea.append(temp)


def dfs(sx, sy, eat, sea):
    global max_fish
    # 상어가 물고기 먹음
    eat += sea[sx][sy][0]
    sea[sx][sy][0] = 0

    # fish 이동
    for fish_num in range(1, 17):
        loc = None
        for x in range(4):
            for y in range(4):
                # 물고기 찾으면 loc 저장
                if sea[x][y][0] == fish_num:
                    loc = (x, y)

        if not loc:
            continue

        x, y = loc
        # 찾은 물고기 방향 저장
        fish_dir = sea[x][y][1]

        for k in range(8):
            nd = (fish_dir + k) % 8
            dx, dy = dir[nd]
            nx, ny = x + dx, y + dy
            # 격자 안에 있어야하고, 이동하는 곳에 상어가 없어야함
            if not (0 <= nx < 4 and 0 <= ny < 4) or ((nx, ny) == (sx, sy)):
                continue
            sea[x][y][1] = nd
            # 물고기 위치 변경
            sea[x][y], sea[nx][ny] = sea[nx][ny], sea[x][y]
            break

    max_fish = max(max_fish, eat)
    shark_dir = sea[sx][sy][1]

    # 상어 이동
    for m in range(1, 4):
        dx, dy = dir[shark_dir]
        nx, ny = sx + (dx * m), sy + (dy * m)
        # 격자 범위 내에 있어야 하고, 물고기 있어야함
        if (0 <= nx < 4 and 0 <= ny < 4) and sea[nx][ny][0] > 0:
            dfs(nx, ny, eat, deepcopy(sea))


dfs(0, 0, 0, sea)
print(max_fish)
