# 2606 바이러스
from collections import deque


def bfs(v):
    queue = deque([v])
    visited[v] = True
    cnt = 0
    while queue:
        q = queue.popleft()

        for i in board[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt


C = int(input())
N = int(input())
board = [[] for _ in range(C + 1)]
visited = [False] * (C + 1)
for i in range(N):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

for i in range(1, C + 1):
    board[i].sort()

print(bfs(1))
