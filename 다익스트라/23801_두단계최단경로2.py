# 두단계 최단 경로 2
import sys, heapq

input = sys.stdin.readline
INF = float("INF")
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
x, z = map(int, input().split())
P = int(input())
Y = list(map(int, input().split()))
mini = INF

def dijkstra(start):
    q = []
    distance = [INF for _ in range(N + 1)]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))
    return distance

dist1, dist2 = dijkstra(x), dijkstra(z)

for ve in Y:
    mini = min(mini, dist1[ve] + dist2[ve])

if mini < INF:
    print(mini)
else:
    print(-1)
