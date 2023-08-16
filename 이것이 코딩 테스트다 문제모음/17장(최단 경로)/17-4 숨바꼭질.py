N, M = 6,7 # 1 <= N <= 20000 노드 수 | 1 <= M <= 50000 간선 수

edges = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]

graph = [[] for _ in range(N+1)]
for start, end in edges:
    graph[start].append(end)
    graph[end].append(start)

INF = 1e9
distances = [INF for _ in range(N+1)]

print(graph)

import heapq

q  = []
start = 0
visited = [False * N+1]
distances[0] = 0
distances[1] = 0

heapq.heappush(q, (0,1)) # (distance, position)

while q:
    distance, position = heapq.heappop(q)
    
    for neighbor in graph[position]:
        if distances[neighbor] < distance + 1: # 방문한 적이 있으면 스킵
            continue
        
        distances[neighbor] = min(distances[neighbor], distance + 1)
        heapq.heappush(q, (distances[neighbor], neighbor))
        
distances = distances[1:]
print(distances)
answer = max(distances)
print(distances.index(answer)+1, answer, distances.count(answer))