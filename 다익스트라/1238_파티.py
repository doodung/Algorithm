# 1238 파ㅌㅣ
import heapq

INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


ans = 0
for i in range(1, N + 1):
    s = dijkstra(i)
    e = dijkstra(X)
    ans = max(ans, s[X] + e[i])
print(ans)
