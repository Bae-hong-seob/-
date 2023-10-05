# N,M = 4,5
# map = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]
N,M = 15,14
map=[
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]

def dfs(start):
    stack = []
    stack.append(start)
    
    while stack:
        row, column = stack.pop()
        if map[row][column] == 0:
            map[row][column] = 1 # 방문 처리
        else:
            continue
        
        if column+1 < M and map[row][column+1] == 0: # 지도 내에 있고 방문하지 않은 경우(오른쪽)
            stack.append([row,column+1])
        if column-1 >= 0 and map[row][column-1] == 0: # 지도 내에 있고 방문하지 않은 경우(왼쪽)
            stack.append([row,column-1])
        if row+1 < N and map[row+1][column] == 0: # 지도 내에 있고 방문하지 않은 경우(아래쪽)
            stack.append([row+1,column])
        if row-1 >= 0 and map[row-1][column] == 0: # 지도 내에 있고 방문하지 않은 경우(위쪽)
            stack.append([row-1,column])
    

candidates = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            candidates.append([i,j])

count = 0
for candidate in candidates:
    i, j = candidate
    if map[i][j] == 0:
        dfs([i,j])
        count+=1

print(count)