from itertools import combinations
from collections import deque
import copy

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

blanks, viruses = [], []
for row in range(N):
    for column in range(M):
        if virus_map[row][column] == 0:
            blanks.append([row,column])
        elif virus_map[row][column] == 2:
            viruses.append([row,column])


answer = 0
candidates = list(combinations(blanks, 3))
for candidate in candidates:
    dq = deque(viruses)
    tmp_map = copy.deepcopy(virus_map)
    
    for row,column in candidate:
        tmp_map[row][column] = 1 # 벽 3개 설치
    
    while dq:
        now = dq.popleft()
        row,column = now
        tmp_map[row][column] = 2 # 방문 = 바이러스 퍼짐
        
        if column+1 <= M-1 and tmp_map[row][column+1] == 0: # 오른쪽 탐색 & 빈칸일 때
            dq.append([row,column+1])
        
        if column-1 >= 0 and tmp_map[row][column-1] == 0: # 왼쪽 탐색 & 빈칸일 때
            dq.append([row,column-1])
        
        if row+1 <= N-1 and tmp_map[row+1][column] == 0: # 위쪽 탐색 & 빈칸일 때
            dq.append([row+1,column])
        
        if row-1 >= 0 and tmp_map[row-1][column] == 0: # 아럐쪽 탐색 & 빈칸일 때
            dq.append([row-1,column])
    
    safe = 0
    for row in tmp_map:
        safe+=row.count(0)
    answer = max(answer, safe)
    
print(answer)