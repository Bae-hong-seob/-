N, M, C = 3,2,1 # 1 <= N <= 30,000 , 1 <= M <= 200,000 , 1 <= C <= N

graph = [
    [],
    [(2,4),(3,2)],
    [],
    []
]

# solution
import heapq

INF = int(1e9)
distances = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]

q = []
heapq.heappush(q, (0,C)) # (distance, city_number)

while q:
    distance, city_number = heapq.heappop(q)
    visited[city_number] = True
    
    if distances[city_number] < distance:
        continue
    
    for neighbor_number, dist in graph[city_number]:
        if distances[neighbor_number] > distance + dist and visited[neighbor_number] == False: # 거쳐가는게 나을 떄 + 방문한 적 없을 때
            distances[neighbor_number] = distance + dist
            heapq.heappush(q, (distances[neighbor_number], neighbor_number))
            
print(distances)

count_city = sum([1 for distance in distances if distance != INF])
count_time = max([distance for distance in distances if distance != INF])
print(count_city,count_time)