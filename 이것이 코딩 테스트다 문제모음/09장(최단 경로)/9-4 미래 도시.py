# N,M = 5,7 # 1 <= N,M <= 100 (N,M) : (전체 회사의 개수, 경로의 개수)
# X,K = 4,5 # 1 <= K <= 100

N,M = 4,2
X,K = 3,4

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int,input().split())
    graph[start][end] = 1 # 양방향 그래프
    graph[end][start] = 1
    
for i in range(N):
    graph[i][i] = 0
    
    
# 1번 노드에서 출발 K까지 최단경로 + K에서 X 최단경로
for k in range(1,N+1): # 모든 노드에 대해 반복
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
if graph[1][K] + graph[K][X] >= INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])