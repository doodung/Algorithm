# 1260
# DFS와 BFS

from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
