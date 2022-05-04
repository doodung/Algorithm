from collections import deque


def BFS(x, y, cost, direction, N, board):
    INF = int(1e9)
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    visited = [[INF] * N for _ in range(N)]
    q = deque()
    q.append((x, y, cost, direction))
    visited[x][y] = cost

    while q:
        x, y, cost, direction = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                if i == direction:
                    next_cost = cost + 100
                else:
                    next_cost = cost + 600
                if next_cost < visited[nx][ny]:
                    visited[nx][ny] = next_cost
                    q.append((nx, ny, next_cost, i))
    return visited[-1][-1]


def solution(board):
    answer = 0
    N = len(board)
    answer = min(BFS(0, 0, 0, 0, N, board), BFS(0, 0, 0, 1, N, board))

    return answer