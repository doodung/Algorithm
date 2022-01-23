# 2644 촌수계산
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        q = queue.popleft()
        for i in board[q]:
            if not visited[i]:
                visited[i] = True
                answer[i] = answer[q] + 1
                queue.append(i)

N = int(input())
I, J = map(int, input().split())
board = [[] for _ in range(N + 1)]
answer = [0 for i in range(N + 1)]

for i in range(int(input())):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0] * (N + 1)

bfs(I)
print(answer[J] if answer[J]!=0 else -1)