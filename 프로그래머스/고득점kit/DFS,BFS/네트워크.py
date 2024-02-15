from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        visited[now] = True # 방문처리
        for neighbor in graph[now]:
            if visited[neighbor] == False:
                queue.append(neighbor)
        
        
def solution(n, computers):
    visited = [False]*n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]==1:
                graph[i].append(j)
    
    count = 0
    for start in range(n):
        if visited[start] == False:
            bfs(graph, start, visited)
            count+=1
            
    return count