N, M = 6,6 # 2 <= N <= 500 | 2 <= M <= 10000 노드수, 간선수
edges = [[1,5],[3,4],[4,2],[4,6],[5,2],[5,4]]

INF = 1e9
graph = [[INF] * (N+1) for _ in range(N+1)]

for start,end in edges:
    graph[start][end] = 1 # 간선이 존재함.

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
count = 0


graph = graph[1:]
final_graph = []

for row in graph:
    row = row[1:]
    row = [0 if value == INF else 1 for value in row]
    # print(row)
    final_graph.append(row)
    
for student in range(N):
    # print(sum(final_graph[student][:]), sum([value[student] for value in final_graph]))
    
    if sum(final_graph[student][:]) + sum([value[student] for value in final_graph]) == N-1: #자기자신 제외
        count+=1
print(count)
