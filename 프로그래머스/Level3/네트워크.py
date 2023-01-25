def solution(n, computers):
    
    visited = [False]*n
    count = 0
    
    def dfs(node): #dfs는 재귀적인 방식을 통해 구현함을 기억
        visited[node] = True
        
        for i in range(n):
            if visited[i] == False and computers[node][i] == True: #방문한적 없음 and 둘은 이웃노드인 경우
                dfs(i)
                
    for node in range(n): #모든 노드에 대해 탐색
        if visited[node] == False:
            dfs(node)
            count+=1
            
    return count
