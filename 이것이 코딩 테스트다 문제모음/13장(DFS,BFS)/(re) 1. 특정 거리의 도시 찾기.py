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

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = list(map(int, input().split()))
    graph[start].append(end)

from collections import deque

distances = {}
distance = 0
distances[X] = distance

# distances = [1e9 for _ in range(N+1)]

visited = [False] * (N+1)

q = deque()
q.append([X,0]) # 시작점 추가

while q:
    now, distance = q.popleft()
    
    if visited[now] == True:
        continue
    else:
        visited[now] = True # 방문처리
        
    for neighbor in graph[now]:
        try:
            distances[neighbor] = min(distances[neighbor], distance+1)
        except:
            distances[neighbor] = distance+1
        q.append([neighbor,distance+1])

distance_k_citys = sorted([city for city in distances if distances[city] == K])
if len(distance_k_citys) == 0:
    print(-1)
else:
    for distance_k_city in distance_k_citys:
        print(distance_k_city)
        
# if distances.count(K) == 0:
#     print(-1)
# else:
#     for city_idx, distance in enumerate(distances):
#         if distance == K:
#             print(city_idx)