# 23290 마법사상어와복제
# 물고기의 수 , 상어가 마법을 연습한 횟수
import copy

M, S = map(int, input().split())
# 물고기의 정보 fx,fy,d -> 물고기위치,방향임
fish_info = [list(map(int, input().split())) for i in range(M)]
# 상어 위치
sx, sy = map(int, input().split())
shark = (sx - 1, sy - 1)
# S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력
ans = 0

# 물고기 방향
fd = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 상어 방향 상,하,좌,우
sd = [(-1, 0), (0, -1), (1, 0), (0, 1)]
fish = fish_info


def moveFish():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while fish[x][y]:
                d = fish[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + fd[i][0], y + fd[i][1]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res


# 백트래킹
# 가능한 이동 방법 중 제외되는 물고기의 수가 가장 많은 방법
# 여러가지일경우, 사전 순으로 -> 백트래킹 시 자동
# 이동한 좌표 == 물고기 냄새 좌표
def maxEat(x, y, dep, cnt, visit):
    global max_eat, shark, eat
    if dep == 3:  # 3번 이동한 경우 stop
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + sd[d][0]
        ny = y + sd[d][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:
                visit.append((nx, ny))
                maxEat(nx, ny, dep + 1, cnt + len(fish[nx][ny]), visit)
                visit.pop()
            else:
                maxEat(nx, ny, dep + 1, cnt, visit)


smell = [[0] * 4 for _ in range(4)]
board = [[[] for _ in range(4)] for _ in range(4)]
fish_change = [[[] for _ in range(4)] for _ in range(4)]
for x, y, d in fish_info:
    board[x - 1][y - 1].append(d - 1)

for _ in range(S):
    fish = copy.deepcopy(board)
    fish = moveFish()
    max_eat = -1
    eat = list()
    maxEat(shark[0], shark[1], 0, 0, list())
    for x, y in eat:
        if fish[x][y]:
            fish[x][y] = []
            smell[x][y] = 3

    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    for i in range(4):
        for j in range(4):
            board[i][j] += fish[i][j]

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(board[i][j])
print(ans)
