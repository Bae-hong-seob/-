def dfs(graph, stack, shape, count, answers):
    # shape : 'width' or 'height' 가로 or 세로
    head, tail = stack.pop()
    head_row, head_column = head
    tail_row, tail_column = tail
    
    if head_row==len(graph)-1 or head_column==len(graph)-1 or tail_row==len(graph)-1 or tail_column == len(graph)-1:
        answers.append(count)
        return
        
    if shape == 'width': # 가로로 놓아져있을 경우
        head_column, tail_column = max(head_column, tail_column), min(head_column, tail_column) # 오른쪽에 있는게 head.
        if head_row <= len(graph)-2: # 아래쪽 방향 탐색
            if graph[head_row+1][head_column]==0 and graph[tail_row+1][tail_column]==0: 
                stack.append([[head_row+1, head_column],[tail_row+1, tail_column]])
                count+=1
                dfs(graph, stack, shape, count, answers)
        
        if head_column <= len(graph)-2: # 오른쪽 방향 탐색
            if graph[head_row][head_column+1]==0: 
                stack.append([[head_row, head_column+1], [tail_row, tail_column+1]])
                count+=1
                dfs(graph, stack, shape, count, answers)
        
        if head_row <= len(graph)-2: 
            if graph[head_row+1][head_column]==0 and graph[tail_row+1][tail_column]==0: 
                shape = 'height'
                count+=1
                
                #head 기준 회전
                stack.append([[head_row, head_column], [tail_row+1, tail_column+1]]) # 반시계방향 90도
                dfs(graph, stack, shape, count, answers)
                # tail 기준 회전
                stack.append([[head_row+1, head_column-1], [tail_row, tail_column]]) # 시계방향 90도
                dfs(graph, stack, shape, count, answers)
        
        # head기준 회전
        if tail_row >= 1:
            if graph[head_row-1][head_column]==0 and graph[tail_row-1][tail_column]==0: 
                stack.append([[head_row, head_column], [tail_row-1, tail_column+1]]) # 시계방향 90도
                dfs(graph, stack, shape, count, answers)
                
                # tail 기준 회전
                stack.append([[head_row-1, head_column-1], [tail_row, tail_column]]) # 반시계방향 90도
                dfs(graph, stack, shape, count, answers)

            
    if shape == 'height':
        head_row, tail_row = max(head_row, tail_row), min(head_row, tail_row) #아래쪽에 있는게 head
        if head_row <= len(graph)-2: # 아래쪽 방향 탐색
            if graph[head_row+1][head_column] == 0:
                stack.append([[head_row+1, head_column],[tail_row+1, tail_column]])
                count+=1
                dfs(graph, stack, shape, count, answers)
                
        if head_column <= len(graph)-2: # 오른쪽 방향 탐색
            if graph[head_row][head_column+1]==0 and graph[tail_row][tail_column+1]==0:
                stack.append([[head_row, head_column+1], [tail_row, tail_column+1]])
                count+=1
                dfs(graph,stack,shape,count, answers)
                
        if head_column <= len(graph)-2: # 시계방향 회전 가능한지
            if graph[head_row][head_column+1]==0 and graph[tail_row][tail_column+1]==0:
                shape = 'width'
                stack.append([[head_row,head_column], [tail_row+1, tail_column+1]])
                count+=1
                dfs(graph,stack,shape,count, answers)
            
    

def solution(board):
    # for row in board:
    #     print(row)
        
    # 모든 경로중에 최솟값? 
    # 어처피 (1,1) 에서 (N,N) 으로 가는거니까.. 회전은 오른쪽, 아래로만.
    # 오른쪽 축 반시계방향 90도 혹은 아래쪽 축 시계방향 90도 
    # 이거는 dfs 각. -> stack
    
    start_point = [[[0,1],[0,0]]] # head, tail순서
    answers = []
    count = 0
    shape = 'width'

    dfs(board, start_point, shape, count, answers)
    
    answer = min(answers)
    return answer