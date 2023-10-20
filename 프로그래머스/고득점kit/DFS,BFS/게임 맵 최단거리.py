from collections import deque

def solution(maps):
    dq = deque([])
    dq.append([0,0,1])
    answers = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    while dq:
        row, column, count = dq.popleft()
        if visited[row][column] == True:
            continue
        else:
            visited[row][column] = True
        if row == len(maps)-1 and column == len(maps[0])-1: # 도착지점인 경우
            answers.append(count)
            continue
            
        if column + 1 < len(maps[0]) and maps[row][column+1] == 1: # 오른쪽 방문하는 경우
            dq.append([row,column+1,count+1])
            
        if row + 1 < len(maps) and maps[row+1][column] == 1: # 아래 방문하는 경우
            dq.append([row+1,column,count+1])
        
        if column - 1 >= 0 and maps[row][column-1] == 1: # 왼쪽 방문하는 경우
            dq.append([row,column-1,count+1])
            
        if row - 1 >= 0 and maps[row-1][column] == 1: # 위쪽 방문하는 경우
            dq.append([row-1,column,count+1])
        
    if len(answers)==0:
        return -1
    else:
        return min(answers)
    return answers