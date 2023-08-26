# 노드의 개수와 간선의 개수 입력받기
n,m = 7,11
# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
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
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노르르 찾을 떄까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(n)] # 초기 부모는 자기자신으로 초기화
edges.sort(key=lambda x:x[2])
    
# 간선을 비용순으로 정렬
total = 0 # 전체 가로등 비용
result = 0

# 간선을 하나씩 확인하며
for edge in edges:
    a,b,cost = edge
    total+=cost
    
    # 사이크링 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost

print(total - result)