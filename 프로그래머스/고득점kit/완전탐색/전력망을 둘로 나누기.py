from collections import deque

def bfs(graph, queue, visited):
    node = 0
    while queue:
        now = queue.popleft()
        visited[now] = True
        node += 1 #해당 그래프 노드 수 
        
        for neighbor in graph[now]:
            if visited[neighbor] == False: #방문한 적이 없다면 추가
                queue.append(neighbor)
                
    return node, visited

def solution(n, wires):
    answer = 1e9
    for idx, wire in enumerate(wires):
        new_wires = wires[:idx] + wires[idx+1:]
        
        graph = [[] for _ in range(n+1)] #0번 노드는 비워둠
        for v1, v2 in new_wires: #전선들 중 하나 끊은 걸로 그래프 구성
            graph[v1].append(v2)
            graph[v2].append(v1)
                
        visited = [False]*(n+1) #방문기록 생성
        nodes = []
        for node in range(1,n+1): #노드 탐색. 노드 번호는 1번부터 n까지
            if visited[node] == False: #새로운 그래프 시작점인 경우
                queue = deque()
                queue.append(node)
                node, visited = bfs(graph, queue, visited)
                nodes.append(node)
            else:
                continue
        different = abs(nodes[0] - nodes[1])
        answer = min(answer, different)
        
    return answer