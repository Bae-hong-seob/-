from collections import deque

def bfs(maps):
    n,m = len(maps), len(maps[0])
    queue = deque([])
    queue.append([0,0])
    drow, dcolumn = [0,-1,0,1],[1,0,-1,0]
    
    while queue:
        row, column = queue.popleft()
        if row==n and column==m: #도착한 경우
            break
        
        for i in range(4): #네 방향 모두 탐색
            new_row, new_column = row+drow[i], column+dcolumn[i]
            if new_row<0 or new_row>n-1 or new_column<0 or new_column>m-1: #지도에서 벗어나는 경우
                continue
            if maps[new_row][new_column] == 0: #벽이 있는 자리
                continue
            if maps[row][column]+1 >= maps[new_row][new_column]: #최단거리가 아닌경우
                continue
            else:
                maps[new_row][new_column] = maps[row][column]+1
                queue.append([new_row, new_column])
            

def solution(maps):    
    n,m = len(maps), len(maps[0])
    for i in range(n): #최대 100*100 = 10,000
        for j in range(m):
            if i==0 and j ==0: #캐릭터 시작점
                continue
            if maps[i][j] == 1:
                maps[i][j] = 100000 # dp_table 최대값으로 초기화.
                
    bfs(maps)
        
    if maps[n-1][m-1] == 0 or maps[n-1][m-1] == 100000:
        return -1
    else:
        return maps[n-1][m-1]
