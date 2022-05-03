import heapq

INF = int(1e9)
V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    # u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻.
distance = [INF] * (V + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
