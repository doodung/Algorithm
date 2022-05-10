from collections import deque

# 5014 스타트링크
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)
q = deque()
q.append(S)
visited[S] = 0
nx = 0
while q:
    x = q.popleft()
    if 1 <= x - D and visited[x - D] == -1:
        nx = x - D
        visited[nx] = visited[x] + 1
        q.append(nx)
    if x + U <= F and visited[x + U] == -1:
        nx = x + U
        visited[nx] = visited[x] + 1
        q.append(nx)

if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])
