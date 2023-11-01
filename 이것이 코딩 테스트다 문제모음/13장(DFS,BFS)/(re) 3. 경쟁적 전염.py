from collections import deque

# N,K = 3,3 # 1 <= N <= 200 , 1 <= K <= 1000
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

# starts = []
# for k in range(1,K+1):
#     for row in range(N):
#         for column in range(N):
#             if virus_map[row][column] == k:
#                 starts.append([k,row,column])
                
starts = [[virus_map[row][column], row, column] for row in range(N) for column in range(N) if virus_map[row][column] != 0]

starts.sort()
starts = deque(starts)

s = 0
while starts:
    if s >= S: # S범위를 보면 0일 수도 있으므로 맨 위에 와야함.
        break
    
    for _ in range(len(starts)):
        k, row,column = starts.popleft()
        
        if column+1 <= N-1 and virus_map[row][column+1] == 0: # 오른쪽 탐색 & 비어있는 경우
            virus_map[row][column+1] = k # 방문처리
            starts.append([k,row,column+1])
        
        if column-1 >= 0 and virus_map[row][column-1] == 0: # 왼쪽 탐색 & 비어있는 경우
            virus_map[row][column-1] = k # 방문처리
            starts.append([k,row,column-1])
            
        if row+1 <= N-1 and virus_map[row+1][column] == 0: # 위쪽 탐색 & 비어있는 경우
            virus_map[row+1][column] = k # 방문처리
            starts.append([k,row+1,column])
        
        if row-1 >= 0 and virus_map[row-1][column] == 0: # 아래쪽 탐색 & 비어있는 경우
            virus_map[row-1][column] = k # 방문처리
            starts.append([k,row-1,column])
    s+=1        

for row in virus_map:
    print(row)
print(virus_map[X-1][Y-1])