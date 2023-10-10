N,M = 5,7
edges = [
    [1,2],
    [1,3],
    [1,4],
    [2,4],
    [3,4],
    [3,5],
    [4,5],
]
X,K = 4,5

# N,M = 4,2
# edges = [
#     [1,3],
#     [2,4]
# ]
# X,K = 3,4

INF = 1e9
dp_table = [[INF]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)] # 도시 번호는 1번부터, 인접리스트로 표현

for edge in edges:
    start, end = edge
    graph[start].append(end)
    dp_table[start][end] = 1
    dp_table[end][start] = 1

for a in range(N):
    for b in range(N):
        if a==b:
            dp_table[a][b] = 0
            
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp_table[i][j] = min(dp_table[i][j], dp_table[i][k]+dp_table[k][j])
            
print(dp_table[1][K])
print(dp_table[K][X])
if dp_table[1][K]+dp_table[K][X] >= INF:
    print(-1)
else:
    print(dp_table[1][K]+dp_table[K][X])