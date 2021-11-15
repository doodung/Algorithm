#19236

from copy import deepcopy

def solve(sx, sy, eat, seaa):
    global answer
    eat += seaa[sx][sy][0]
    seaa[sx][sy][0] = 0

    for num_fish in range(1, 17):
        loc = None
        for x in range(4):
            for y in range(4):
                if seaa[x][y][0] == num_fish:
                    loc = (x, y)

        if not loc:
            continue

        x, y = loc
        fish = seaa[x][y][1]

        for k in range(8):
            nd = (fish + k) % 8
            dx, dy = dirs[nd]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 4 and 0 <= ny < 4) or ((nx, ny) == (sx, sy)):
                continue
            seaa[x][y][1] = nd
            seaa[x][y], seaa[nx][ny] = seaa[nx][ny], seaa[x][y]
            break

    answer = max(answer, eat)
    shark = seaa[sx][sy][1]
    for move in range(1, 4):
        dx, dy = dirs[shark]
        nx, ny = sx + (dx * move), sy + (dy * move)
        if (0 <= nx < 4 and 0 <= ny < 4) and seaa[nx][ny][0] > 0:
            solve(nx, ny, eat, deepcopy(seaa))


answer = 0
dirs = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

space = [list(map(int, input().split())) for _ in range(4)]
sea = []
for i in range(4):
    row = []
    for j in range(0, 8, 2):
        row.append([space[i][j], space[i][j + 1] - 1])
    sea.append(row)

solve(0, 0, 0, sea)
print(answer)