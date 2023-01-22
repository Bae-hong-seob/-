def solution(n, computers):
    
    def dfs(v):
        visited[v] = True

        for nei in range(n):    # 인접노드 탐구 
            if not visited[nei] and computers[v][nei]:    # unvisited + 인접할 때 
                dfs(nei)
        
    count = 0   
    visited = [False] * (n)   

    for node_idx in range(n):
        if not visited[node_idx] :
            dfs(node_idx)
            count += 1         # dfs 끝나면 count 해주기 

    return count