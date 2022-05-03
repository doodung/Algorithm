from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(p):
    for x in range(5):
        for y in range(5):
            if p[x][y] == 'P':
                visited = [[0] * 5 for i in range(5)]
                q = deque()
                q.append((x, y, 0))
                visited[x][y] = True
                while q:
                    x, y, dist = q.popleft()
                    if 0 < dist < 3 and p[x][y] == 'P':
                        return 0
                    if dist > 2:
                        break
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        nd = dist + 1
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if not visited[nx][ny] and p[nx][ny] != 'X':
                                q.append((nx, ny, nd))
                                visited[nx][ny] = True
    return 1


def solution(places):
    answer = []
    for p in places:
        answer.append(BFS(p))

    return answer