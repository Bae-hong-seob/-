N,M = 5,6 # N은 세로 M은 가로
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

def dfs(graph, stack):
    if stack[0] == end:
        return
    print(stack)
    if len(stack) == 1: # 시작점일 경우 past가 없음
        print('here')
        now_row, now_column = stack[0]
        
        if now_row < N-1: # 아래 방향 탐색
            if graph[now_row+1][now_column] >= 1: # 괴물이 없는 경우
                stack.append([now_row+1, now_column]) # 방문 노드 삽입
                dfs(graph, stack)
        
        if now_column < M-1: # 오른쪽 방향 탐색
            if graph[now_row][now_column+1] >= 1: # 괴물이 없는 경우
                stack.append([now_row, now_column+1]) # 방문 노드 삽입
                dfs(graph, stack)
    
    else:# 시작점이 아닐 경우
        past_row, past_column = stack.pop(0)
        now_row, now_column = stack[0]
        print('now : update ,', graph[now_row][now_column], graph[past_row][past_column])
        print('now position : ', [now_row, now_column])
        graph[now_row][now_column] =  graph[past_row][past_column]+1 # 현재 경로 길이 업데이트
        
        if now_row < N-1: # 아래 방향 탐색
            if graph[now_row+1][now_column] >= 1: # 괴물이 없는 경우
                stack.append([now_row+1, now_column]) # 방문 노드 삽입
                dfs(graph, stack)
        
        if now_column < M-1: # 오른쪽 방향 탐색
            if graph[now_row][now_column+1] >= 1: # 괴물이 없는 경우
                stack.append([now_row, now_column+1]) # 방문 노드 삽입
                dfs(graph, stack)


stack = [[3,0]]
end = [4,5]

dfs(graph, stack)        
print(graph[N-1][M-1])