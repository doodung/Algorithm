# 스타트택시
from collections import deque

N, M, Oil = map(int, input().split())
# 지도 0은 빈칸 1은 벽 -> 못지나감
board = [list(map(int, input().split())) for i in range(N)]
# 운전을 시작하는 행번호와 열번호
taxi_x, taxi_y = map(lambda x: int(x) - 1, input().split())
people_info = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
people_start, people_end = [], []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for m in range(M):
    sx, sy, ex, ey = people_info[m]
    people_start.append([sx, sy])
    people_end.append([ex, ey])


# 승객까지의 최단거리 찾기
def loadBFS(x, y):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    mini_people = []
    mini = float('inf')
    while q:
        x, y = q.popleft()
        if visited[x][y] > mini:
            break
        if [x, y] in people_start:
            mini = visited[x][y]
            mini_people.append([x, y])
        else:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    if mini_people:
        mini_people.sort()
        return visited[mini_people[0][0]][mini_people[0][1]], mini_people[0]
    else:
        return -1, -1


# 출발지에서 도착지까지의 최단거리 찾기
def taxiBFS(s, e):
    x, y = s
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    load_taxi = -1
    while q:
        x, y = q.popleft()
        if [x, y] == e:
            load_taxi = visited[x][y]
            break
        else:
            for dd in range(4):
                nx = x + dx[dd]
                ny = y + dy[dd]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return load_taxi


index, dis, p = 0, 0, 0
for m in range(M):
    dis, p = loadBFS(taxi_x, taxi_y)
    if Oil - dis < 0 or dis < 0:
        Oil = -1
        break
    Oil -= dis
    # 최단거리에 있는 손님의 인덱스를 찾는다
    if p in people_start:
        index = people_start.index(p)
    # 도착지
    end = people_end[index]
    # 보드에 있는 손님을 지움
    board[p[0]][p[1]] = 0
    load = taxiBFS(p, end)
    if Oil - load < 0 or load < 0:
        Oil = -1
        break
    # 잘 데려다주면 걸린 길이의 2배
    Oil = (Oil - load) + load * 2
    # start, pop 배열에서 없애준다
    people_start.pop(index)
    people_end.pop(index)
    # 도착지가 다시 택시의 출발지가 된다
    taxi_x, taxi_y = end

# 남은 오일 출력
print(Oil)
