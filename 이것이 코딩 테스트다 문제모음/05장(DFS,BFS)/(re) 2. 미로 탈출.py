# N,M = 5,6 # N은 세로 M은 가로
# graph = [
#     [1,0,1,0,1,0],
#     [1,1,1,1,1,1],
#     [0,0,0,0,0,1],
#     [1,1,1,1,1,1],
#     [1,1,1,1,1,1]
# ]

N,M=3,3
graph = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]

count = 0
exit = False

def dfs(stack):
    global exit
    global count
    
    row, column = stack.pop()
    count+=1
    
    if row == N-1 and column == M-1: # 출구에 도착 시 종료
        exit = True
        return True
        
    if  row+1 < N and graph[row+1][column] == 1 and exit == False: # 괴물이 없는 곳 + 지도 내에 위치한 경우(아래쪽)
        stack.append([row+1, column])
        dfs(stack)
    
    if column+1 < M and graph[row][column+1] == 1 and exit == False: # 괴물이 없는 곳 + 지도 내에 위치한 경우(오른쪽)
        stack.append([row,column+1])
        dfs(stack)
        
    if row-1 >= 0 and graph[row-1][column] == 1 and exit == False: # 괴물이 없는 곳 + 지도 내에 위치한 경우(위쪽)
        stack.append([row-1,column])
        dfs(stack)
    
    if column-1 >= 0 and graph[row][column-1] == 1 and exit == False: # 괴물이 없는 곳 + 지도 내에 위치한 경우(왼쪽)
        stack.append(row,column-1)
        dfs(stack)

stack = []
stack.append([0,0])
dfs(stack)
print(count)