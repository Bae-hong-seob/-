# N = 5 # 3 <= N <= 6 map 크기.(N * N)
# graph = [
#     ['X','S','X','X','T'],
#     ['T','X','S','X','X'],
#     ['X','X','X','X','X'],
#     ['X','T','X','X','X'],
#     ['X','X','T','X','X']]

# N = 4
# graph = [
#     ['S','S','S','T'],
#     ['X','X','X','X'],
#     ['X','X','X','X'],
#     ['T','T','T','X']
# ]

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))
                 
                 
from itertools import combinations

teachers = [[row,column] for row in range(N) for column in range(N) if graph[row][column] == 'T']
candidates = list(combinations([[row,column] for row in range(N) for column in range(N) if graph[row][column] == 'X'], 3))
directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# 선생님 한명은 상,하,좌,우 모두 탐색함. dfs가 맞다는 생각. =stack.
def dfs(graph, direction, stack):
    global N
    
    #print('start point : ',stack)
    row, column = stack[-1]
    
    if row >= 1 and direction == 'UP': # 위쪽 방향으로 전진
        if graph[row-1][column] == 'X' or graph[row-1][column] == 'T': # 위에 아무것도 없을 경우 혹은 다른 선생님 시야 안일 경우
            graph[row-1][column] = 'T' # 방문처리
            stack.append([row-1, column]) # 이동
            result, graph = dfs(graph, 'UP', stack)
            
            if result == False:
                return False, graph
            
        elif graph[row-1][column] == 'S': # 학생 발견시 종료
            return False, graph
        
                    
            
    if row <= N-2 and direction == 'DOWN': #아래쪽 방향으로 전진
        if graph[row+1][column] == 'X' or graph[row+1][column] == 'T': #아래에 아무것도 없을 경우 혹은 다른 선생님 시야 안인 경우
            graph[row+1][column] = 'T' # 방문처리
            stack.append([row+1, column]) # 이동
            result, graph = dfs(graph, 'DOWN', stack)
            
            if result == False:
                return False, graph
            
        elif graph[row+1][column] == 'S': # 학생 발견시 종료
            return False, graph
        
    if column >= 1 and direction == 'LEFT': # 왼쪽 방향으로 전진
        if graph[row][column-1] == 'X' or graph[row][column-1] == 'T': # 왼쪽에 아무것도 없을 경우 혹은 다른 선생님 시야 안인 경우
            graph[row][column-1] = 'T' # 방문처리
            stack.append([row, column-1])
            result, graph = dfs(graph, 'LEFT', stack)
            
            if result == False:
                return False, graph
            
        elif graph[row][column-1] == 'S': # 학생 발견시 종료
            return False, graph
        
    if column <= N-2 and direction == 'RIGHT': # 오른쪽 방향으로 전진
        if graph[row][column+1] == 'X' or graph[row][column+1] == 'T': # 오른쪽에 아무것도 없을 경우 혹은 다른 선생님 시야 안인 경우
            graph[row][column+1] = 'T' # 방문처리
            stack.append([row, column+1])
            result, graph = dfs(graph, 'RIGHT', stack)
            
            if result == False:
                return False, graph
            
        elif graph[row][column+1] == 'S': # 학생 발견시 종료
            return False, graph
    
    if len(stack) > 1: # 출발지점은 삭제 x
        stack.pop()
        
    return True, graph
        

# for row in graph:
#     print(row)


for candidate in candidates: # 벽을 세울 수 있는 후보군 하나
    temp_graph = [row.copy() for row in graph] # 임시 그래프 생성
    
    for row, column in candidate: # 3개 벽 설치
        temp_graph[row][column] = 'O'
        
    result = True

    for teacher in teachers:
        stack = []
        stack.append(teacher)
        for direction in directions:
            result, temp_graph = dfs(temp_graph, direction, stack)
            if result == False:
                break
        
        if result == False:
            break
        
    if result == False:
        continue
    elif result == True:
        break

if result == True:
    print('YES')
elif result == False:
    print('NO')
else:
    print('Error') 
#print(result)
# for candidate in candidates: # 벽을 세울 수 있는 후보군 하나
#     temp_graph = [row.copy() for row in graph] # 임시 그래프 생성
    
#     for row, column in candidates: # 3개 벽 설치
#         temp_graph[row][column] = 'O'
        
#     for teacher in teachers: # 모든 선생님에 대하여 dfs수행이 나을듯?