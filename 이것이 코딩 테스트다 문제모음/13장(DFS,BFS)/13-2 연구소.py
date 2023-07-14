from itertools import combinations
from collections import deque

N, M = map(int, input().split())
virus_map = []
for _ in range(N):
    row = list(map(int,input().split()))
    virus_map.append(row)
    
# N,M = 7,7
# virus_map = [
#     [2,0,0,0,1,1,0],
#     [0,0,1,0,1,2,0],
#     [0,1,1,0,1,0,0],
#     [0,1,0,0,0,0,0],
#     [0,0,0,0,0,1,1],
#     [0,1,0,0,0,0,0],
#     [0,1,0,0,0,0,0],
# ]

# N,M = 4,6
# virus_map = [
#     [0,0,0,0,0,0],
#     [1,0,0,0,0,2],
#     [1,1,1,0,0,2],
#     [0,0,0,0,0,2]
# ]

# N,M = 8,8
# virus_map = [
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [0,0,0,0,0,0,0,0],    
#     [0,0,0,0,0,0,0,0],    
#     [0,0,0,0,0,0,0,0],    
# ]

def bfs(graph, queue):
    
    while queue:
        row, column = queue.popleft()
        
        if row >= 1: # 위쪽 방향 탐색
            if graph[row-1][column] == 0: # 빈칸이라면
                graph[row-1][column] = 2 # 바이러스 퍼짐(=방문 처리)
                queue.append([row-1, column])
                
        if row < N-1: # 아래쪽 방향 탐색
            if graph[row+1][column] == 0: # 빈칸이라면
                graph[row+1][column] = 2 # 바이러스 퍼짐(=방문 처리)
                queue.append([row+1, column])
                
        if column >= 1: # 왼쪽 방향 탐색
            if graph[row][column-1] == 0: # 빈칸이라면
                graph[row][column-1] = 2 # 바이러스 퍼짐(=방문 처리)
                queue.append([row, column-1])
                
        if column < M-1: # 오른쪽 방향 탐색
            if graph[row][column+1] == 0: # 빈칸이라면
                graph[row][column+1] = 2 # 바이러스 퍼짐(=방문 처리)
                queue.append([row, column+1])
                
    return graph

# solution
positions = [[row,column] for row in range(N) for column in range(M) if virus_map[row][column] == 0]
#print(positions)

candidates = list(combinations(positions, 3))
#print(len(candidates))

viruses = [[row,column] for row in range(N) for column in range(M) if virus_map[row][column] == 2]

answers = []

# 일단 벽을 세워
for candidate in candidates: # 모든 조합 가능성에 대해 탐색
    graph = [row.copy() for row in virus_map] # 원본 그래프 virus_map은 그대로 둬야함. 
    
    for row, column in candidate: # 3개 벽 조합 후보군에 대해
        graph[row][column] = 1 # 벽 설치
        
    # 이후에 바이러스 퍼뜨려 -> bfs -> 바이러스가 퍼진 graph 생성
    for viruse in viruses:
        queue = deque()
        queue.append(viruse)
        graph = bfs(graph, queue)
    
    safe_area = sum([row.count(0) for row in graph])
    answers.append(safe_area)

print(max(answers))