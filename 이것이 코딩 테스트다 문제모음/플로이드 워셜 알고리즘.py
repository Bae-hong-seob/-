n,m = 4,7

graph =[
    [],
    [[2,4],[4,6]],
    [[1,3],[3,7]],
    [[1,5],[4,4]],
    [[3,2]]
]

'''
문제: 모든 노드끼리의 최단 거리를 구해야 함.
'''

INF = int(1e9)
distances = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    distances[i][i]=0
for i, row in enumerate(graph):
    for j, cost in row:
        distances[i][j]=cost

for row in distances:
    print(row) 
print()

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            distances[i][j] = min(distances[i][j], distances[i][k]+distances[k][j])

for row in distances:
    print(row)