T = 3 # 1 <= T <= 10 테스트 케이스 수

N = 3 # 2 <= N <= 125 탐사 공간의 크기(N*N)
graph = [
    [5,5,4],
    [3,9,1],
    [3,2,7]
]

# N = 5 # 2 <= N <= 125 탐사 공간의 크기(N*N)
# graph = [
#     [3,7,2,0,1],
#     [2,8,0,9,1],
#     [1,2,1,8,1],
#     [9,8,9,2,0],
#     [3,6,5,1,5]
# ]

# N = 7 # 2 <= N <= 125 탐사 공간의 크기(N*N)
# graph = [
#     [9,0,5,1,1,5,3],
#     [4,1,2,1,6,5,3],
#     [0,7,6,1,6,8,5],
#     [1,1,7,8,3,2,3],
#     [9,4,0,7,6,4,1],
#     [5,8,3,2,4,8,3],
#     [7,4,8,4,8,3,4]
# ]

# solution
# 시작점[0,0] 에서 도착지점[n-1,n-1] 까지 최단거리 -> 다익스트라 알고리즘. 힙구조 이용하는 것. 125 * 125 = 10000 * log 10000

import heapq

q = []
start = [0,0,0]
visited = [[False]*N for _ in range(N)]
INF = int(1e9)
dp_table = [[INF]*N for _ in range(N)]
dp_table[0][0] = graph[0][0] # 시작지점

heapq.heappush(q, start)

while q:
    distance, now_row, now_column = heapq.heappop(q)
    visited[now_row][now_column] = True # 방문처리
    
    # 상 하 좌 우 탐색
    if now_row -1 >= 0: # 상
        # 거쳐가는 것이 나을 떄 
        if dp_table[now_row-1][now_column] > dp_table[now_row][now_column] + graph[now_row-1][now_column] and visited[now_row-1][now_column] == False:
            dp_table[now_row-1][now_column] = dp_table[now_row][now_column] + graph[now_row-1][now_column]
            heapq.heappush(q, (dp_table[now_row-1][now_column], now_row-1, now_column))
            
    if now_row +1 <= N-1: # 하
        # 거쳐가는 것이 나을 때
        if dp_table[now_row+1][now_column] > dp_table[now_row][now_column] + graph[now_row+1][now_column] and visited[now_row+1][now_column] == False:
            dp_table[now_row+1][now_column] = dp_table[now_row][now_column] + graph[now_row+1][now_column]
            heapq.heappush(q, (dp_table[now_row+1][now_column], now_row+1, now_column))
            
    if now_column -1 >= 0: # 좌
        # 거쳐가는 것이 나을 때
        if dp_table[now_row][now_column-1] > dp_table[now_row][now_column] + graph[now_row][now_column-1] and visited[now_row][now_column-1] == False:
            dp_table[now_row][now_column-1] = dp_table[now_row][now_column] + graph[now_row][now_column-1]
            heapq.heappush(q, (dp_table[now_row][now_column-1], now_row, now_column-1))
    
    if now_column +1 <= N-1: #우
        # 거쳐가는 것이 나을 때
        if dp_table[now_row][now_column+1] > dp_table[now_row][now_column] + graph[now_row][now_column+1] and visited[now_row][now_column+1] == False:
            dp_table[now_row][now_column+1] = dp_table[now_row][now_column] + graph[now_row][now_column+1]
            heapq.heappush(q, (dp_table[now_row][now_column+1], now_row, now_column+1))
            
            
print(dp_table[-1][-1])

for row in dp_table:
    print(row)