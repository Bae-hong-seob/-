# N = 5 # 행성의 개수 1 <= N <= 100,000 -> 10,000,000,000
# nodes = [ # x,y,z 좌표
#     [11,-15,-15],
#     [14,-5,-15],
#     [-1,-1,-5],
#     [10,-4,-1],
#     [19,-4,19]
# ]

N = int(input())
nodes = []
for _ in range(N):
    nodes.append(list(map(int,input().split())))

# solution
# N-1개 터널을 건설해서 모든 행성이 서로 연결되게 한다 -> 최소 신장트리
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b: # 부모 index 작은쪽으로 통일
        parent[b] = a
    else:
        parent[a] = b
        
#edges = [[i,j,min(abs(x1-x2), abs(y1-y2), abs(z1-z2))] for i, (x1,y1,z1) in enumerate(nodes) for j,(x2,y2,z2) in enumerate(nodes)]
edges = []
for i in range(N):
    for j in range(i,N):
        x1,y1,z1 = nodes[i]
        x2,y2,z2 = nodes[j]
        edges.append([i,j,min(abs(x1-x2), abs(y1-y2), abs(z1-z2))])
parent = [i for i in range(N)]

edges.sort(key=lambda x:x[2]) # cost순서로 정리

answer = 0
for edge in edges:
    start,end,cost = edge
    if start == end: # 자기자신은 건너뜀
        continue
    
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start,end)
        answer+=cost
        
print(answer)