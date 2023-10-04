N, M = 4,4 # (N x M map)
row, column, direction = 1,1,0
map = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]

visited = [row.copy() for row in map]

def move(row,column,direction):
    if direction == 0: # 북쪽
        drow, dcolumn = row, column-1   
    
    elif direction == 1: # 동쪽
        drow, dcolumn = row-1, column
    
    elif direction == 2: # 남쪽
        drow, dcolumn = row, column+1
    
    elif direction == 3: # 서쪽
        drow, dcolumn = row+1, column
        
    if drow > 0 and drow < N and dcolumn > 0 and dcolumn < N: # move 가능
        return drow,dcolumn
    else: # move 불가능
        return row,column
    

count = 0
end = 0
while end < 4:
    drow, dcolumn = move(row, column, direction)
    
    direction = (direction-1)%4 # 방향전환
    if visited[drow][dcolumn] == 1: # 가본곳이거나 바다
        end+=1 # 종료조건 발동
        if end < 4:
            continue
        else: # 네 방향 모두 가본곳이거나 바다
            direction = (direction-2)%4 # 뒤쪽방향
            drow, dcolumn = move(drow, dcolumn, direction)
            if map[drow][dcolumn] == 1: # 뒤쪽방향이 바다인 경우
                break
            
    else: # 방문
        row,column = drow, dcolumn # 방문
        visited[drow][dcolumn] = 1 # 방문처리
        count+=1
        end = 0 # 종료조건 초기화
        
print(count)