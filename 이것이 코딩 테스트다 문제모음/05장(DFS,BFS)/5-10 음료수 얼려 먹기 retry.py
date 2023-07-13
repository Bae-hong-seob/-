# N, M = 4, 5 # N은 세로길이, M은 가로길이
# graph = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

N,M = 15,14
graph=[
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

# 이동해서 끝까지 가보는 dfs가 맞을 것 같음.
# dfs는 stack. 방문가능하면 삽입. 방문처리.
# 해당 문제에서는 방문처리 = 1 하면 될 듯.
# graph의 x,y 좌표 이용. 2차원 리스트로 표현됨

def dfs(graph, stack):
    row, column = stack.pop()
    graph[row][column] = 1 # 현재 노드 방문 처리(시작점 고려)
    
    if row >= 1: #위쪽 방향 확인
        if graph[row-1][column] == 0: # 구멍이라면
            stack.append([row-1, column]) # 노드 삽입
            graph[row-1][column] = 1 # 방문처리
            dfs(graph, stack) # 재귀함수 시작.
    
    if row < N-1: #아래쪽 방향 확인
        if graph[row+1][column] == 0: # 구멍이라면
            stack.append([row+1, column]) # 노드 삽입
            graph[row+1][column] = 1 # 방문처리
            dfs(graph, stack)
            
    if column >= 1: #왼쪽 방향 확인
        if graph[row][column-1] == 0: # 구멍이라면
            stack.append([row, column-1]) # 노드 삽입
            graph[row][column-1] = 1 # 방문처리
            dfs(graph, stack)
    
    if column < M-1: #오른쪽 방향 확인
        if graph[row][column+1] == 0: # 구멍이라면
            stack.append([row, column+1]) # 노드 삽입
            graph[row][column+1] # 방문처리
            dfs(graph, stack)

number_of_ice_cream = 0            
for row_index, row_values in enumerate(graph):
    for column_index, value in enumerate(row_values):
        if  value == 0: # 구멍인 경우
            stack = [[row_index, column_index]] # 시작점 지정
            dfs(graph, stack)
            number_of_ice_cream+=1
            
print(number_of_ice_cream)