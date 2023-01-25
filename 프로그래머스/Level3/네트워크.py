def solution(n, computers):
    
    visited = [False]*n
    count = 0  
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in range(n): #인접 노드 탐색
            if visited[neighbor] == False and computers[node][neighbor] == 1: #방문 X and 인접노드 일 때 
                dfs(neighbor) 
            else:
                continue
    
    for node_idx in range(n): #모든 노드에 대해 반복 검사
        if visited[node_idx] == False:
            dfs(node_idx)
            count+=1
        else:
            continue
    
    return count
