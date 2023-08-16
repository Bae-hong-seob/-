n = int(input())
m = int(input())

inputs = []

for _ in range(m):
    inputs.append(list(map(int, input().split())))
    
# n = 5 # 1 <= n <= 100 노드 수.
# m = 14 # 1 <= m <= 100000 간선 수

# inputs = [
#     [1,2,2],
#     [1,3,3],
#     [1,4,1],
#     [1,5,10],
#     [2,4,2],
#     [3,4,1],
#     [3,5,1],
#     [4,5,3],
#     [3,5,10],
#     [3,1,8],
#     [1,4,2],
#     [5,1,7],
#     [3,4,2],
#     [5,2,4]
# ]
    
# solution 
# 모든 도시에서 모든 도시로 가는 필요한 최솟값 : 플로이드 워샬. 점화식 기억.
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0
    
for start, end, cost in inputs:
    graph[start][end] = min(graph[start][end], cost) # 노선이 여러개 일 수 있으므로 최솟값으로 업데이트
            
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
graph = graph[1:]
            
for row in graph:
    row = [0 if value == 1e9 else value for value in row]
    row = row[1:]
    for value in row:
        print(value, end=' ')
    print()