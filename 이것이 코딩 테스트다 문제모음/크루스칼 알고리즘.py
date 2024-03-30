n,m = 7,9
graph=[
    [],
    [[2,29],[5,75]],
    [[3,35],[6,34]],
    [[4,7]],
    [[6,23],[7,13]],
    [[6,53]],
    [[7,25]]
]


edges = []
for i, row in enumerate(graph):
    for j,cost in row:
        edges.append([cost,i,j])
edges.sort()

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a,b):
    a = parents[a]
    b = parents[b]
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

parents = [i for i in range(n+1)]
answer = 0
for edge in edges:
    cost, i, j = edge
    if find_parent(parents,i) != find_parent(parents,j):
        print(edge)
        answer+=cost
        union_parent(parents, i,j)
print(parents)
print(answer)