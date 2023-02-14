from collections import deque

def solution(n, edge):
#     box = [[0]*(n+1) for i in range(n+1)]
    
#     for i,j in edge:
#         box[i][j] = 1
#         box[j][i] = 1
        
    box = [[] for i in range(n+1)]
    
    for i,j in edge: #인접행렬 그래프 구축
        box[i].append(j)
        box[j].append(i)
        
    #트리탐색이 좋지 않나?
    visited = [0]*(n+1)
    visited[1] = 1 #1번 노드에서 출발
    dq = deque([1]) #1번 노드에서 출발
    
    while(dq):
        x = dq.popleft()
        for i in box[x]:
            if visited[i]==0:
                visited[i] = visited[x] + 1
                dq.append(i)
                
    max_v = max(visited)
    return visited.count(max_v)