N,M = 7,11 # 1 <= N <= 200.000 집의 수(node) | N-1 <= M <= 200.000 도로 수(edge)
edges = [
    [0,1,7],
    [0,3,5],
    [1,2,8],
    [1,3,9],
    [1,4,7],
    [2,4,5],
    [3,4,15],
    [3,5,6],
    [4,5,8],
    [4,6,9],
    [5,6,11]
]

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N)] # 초기 부모는 자기자신으로 초기화
edges.sort(key=lambda x:x[2])
print(edges)

total = 0
save = 0
for edge in edges:
    start,end,cost = edge
    total+=cost
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        save+=cost

answer = total - save
print(total, save, answer)