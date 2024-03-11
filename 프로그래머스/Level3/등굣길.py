from collections import deque

def dfs(graph, stack, result, length):
    n,m = len(graph), len(graph[0])
    row, column = stack.pop()
    
    if row==n-1 and column==m-1: #도착지점에 다다른 경우 종료.
        result.append(length)
        return
    
    if row < n-1 and column < m-1: #오른쪽, 아래쪽 모두 탐색 가능
        if graph[row][column+1] != -1: #오른쪽으로 진행가능한 경우.
            stack.append([row,column+1])
            dfs(graph, stack, result, length+1)
            
        if graph[row+1][column] != -1: #아래쪽으로 진행가능한 경우
            stack.append([row+1,column])
            dfs(graph, stack, result, length+1)
            
    elif row < n-1: #아래쪽으로만 탐색 가능한 경우
        if graph[row+1][column] != -1:
            stack.append([row+1,column])
            dfs(graph, stack, result, length+1)
    elif column < m-1: #오른쪽으로만 탐색 가능한 경우
        if graph[row][column+1] != -1:
            stack.append([row,column+1])
            dfs(graph, stack, result, length+1)
    else:
        pass
    
    return result
    

def solution(m, n, puddles):
    graph = [[0]*m for _ in range(n)]
    for column,row in puddles:
        graph[row-1][column-1] = -1
        
    # for row in graph:
    #     print(row)
        
    row, column = 0,0
    stack = deque()
    stack.append([row,column])
    result, length = [],0
    result = dfs(graph, stack, result, length)
    
    if len(result) == 0: #갈 수 있는 방법이 없는 경우
        return 0
    else:   
        return result.count(min(result)) % 1000000007