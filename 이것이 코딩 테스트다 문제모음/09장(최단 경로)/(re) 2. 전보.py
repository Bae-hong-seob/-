N,M,C = 3,2,1
edges = [
    [1,2,4],
    [1,3,2]
]

graph = [[] for _ in range(N+1)]
for edge in edges:
    start, end, distance = edge
    graph[start].append((end, distance))
    
visited = [False] * (N+1)
INF = 1e9
distances = [INF]*(N+1)

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (distance, node index)
    distances[start] = 0
    
    while q:
        distance, now = heapq.heappop(q)
        if visited[now] == True:
            continue
        else:
            visited[now] = True
            
        for neighbor, distance in graph[now]:
            cost = distances[now] + distance # 현재까지 거리 + 이웃노드 가는 거리
            if distances[neighbor] > cost:
                distances[neighbor] = cost
                heapq.heappush(q,(cost, neighbor))

dijkstra(C)
print(distances)
print(visited)
count = sum([1 for distance in distances if distance != INF and distance != 0])
max_distance = max([distance for distance in distances if distance != INF])
print(count, max_distance)