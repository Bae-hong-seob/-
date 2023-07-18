# N,M = 3,3 # 1 <= N <= 200 , 1 <= K <= 1000
# virus_map = [[1,0,2], [0,0,0], [3,0,0]]
# S,X,Y = 2,3,2

# N,M = 3,3
# virus_map = [[1,0,2], [0,0,0], [3,0,0]]
# S,X,Y = 1,2,2

N, K = map(int, input().split())
virus_map = []
for _ in range(N):
    virus_map.append(list(map(int, input().split())))
S,X,Y = map(int, input().split())

# solution
from collections import deque

viruses = [[row, column, virus_map[row][column]] for row in range(N) for column in range(N) if virus_map[row][column] != 0]
viruses = sorted(viruses, key=lambda x : x[2]) # 바이러스 번호 작은 순서대로 정렬

# 상하 좌우 한칸씩 모두 이동하는거니까 bfs가 맞는듯 -> queue
def bfs(graph, queue):
    next_position = deque()
    while queue:
        row, column, value = queue.popleft()
        
        if row >= 1: # 위쪽 방향 이동
            if graph[row-1][column] == 0: # 공백일 때 바이러스 이동
                graph[row-1][column] = value # value값으로 바이러스 퍼짐(=방문 처리)
                next_position.append([row-1, column, value]) # 바이러스 이동

                
        if row <= N-2: # 아래쪽 방향 이동
            if graph[row+1][column] == 0: # 공백일 때 바이러스 이동
                graph[row+1][column] = value # value값으로 바이러스 퍼짐(=방문 처리)
                next_position.append([row+1, column, value]) # 바이러스 이동
        if column >= 1: # 왼쪽 방향 이동
            if graph[row][column-1] == 0: # 공백일 때 바이러스 이동
                graph[row][column-1] = value # value값으로 바이러스 퍼짐(=방문 처리)
                next_position.append([row, column-1, value]) # 바이러스 이동
        
        if column <= N-2: # 오른쪽 방향 이동
            if graph[row][column+1] == 0: # 공백일 때 바이러스 이동
                graph[row][column+1] = value # value값으로 바이러스 퍼짐(=방문 처리)
                next_position.append([row,column+1, value]) # 바이러스 이동
                
    return next_position

queue = deque(viruses)

for _ in range(S):
    queue = bfs(virus_map, queue)
    
#print('graph : ', virus_map)
print(virus_map[X-1][Y-1])