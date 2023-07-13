from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = list(map(int, input().split()))
    graph[start].append(end)

# N,M,K,X = 4,4,2,1
# graph = [
#     [],
#     [2,3],
#     [3,4],
#     [],
#     []
# ]

# N,M,K,X = 4,3,2,1
# graph = [
#     [],
#     [2,3,4],
#     [],
#     [],
#     []
# ]

# N,M,K,X = 4,4,1,1
# graph = [
#     [],
#     [2,3],
#     [3,4],
#     [],
#     []
# ]

queue = deque()
queue.append([X,0])

distance = 0
distances = {}
# 최소 거리 탐색은 bfs가 맞는듯. 단계마다 거리 할당.
def bfs(graph, queue, distances):
    visited = [False] * (N+1)
    
    while(queue):
        v, distance = queue.popleft()
        visited[v] = True
        
        for neighbor in graph[v]: # 이웃 노드 관찰
            if visited[neighbor] == False: # 방문한 적이 없다면
                queue.append([neighbor, distance+1])
                visited[neighbor] = True # 방문처리
                
                try: # 이미 계산된 거리가 있으면 최소 거리 업데이트
                    min_distance = min(distances[neighbor], distance+1)
                    distances[neighbor] = min_distance
                except: # 없으면 최소 거리 데이터 생성
                    distances[neighbor] = distance+1
        
    return distances

distances = bfs(graph, queue, distances)

# print(distances)

distance_k_citys = sorted([city for city in distances if distances[city] == K])
if len(distance_k_citys) == 0:
    print(-1)
else:
    for distance_k_city in distance_k_citys:
        print(distance_k_city)