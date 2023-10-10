N,M = 7,8 
inputs = [ #[합치기or여부호가인, a번학생, b번학생]
    [0,1,3],
    [1,1,7],
    [0,7,6],
    [1,7,1],
    [0,3,7],
    [0,4,2],
    [0,1,1],
    [1,1,1]
]

def find_parents(parent, x):
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]

def union_parents(parent, a,b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(N+1)]

answer = []
for input in inputs:
    order, a, b = input
    if order == 0:
        union_parents(parent, a,b)
    elif order == 1:
        if find_parents(parent, a) == find_parents(parent,b):
            answer.append('YES')
        else:
            answer.append('NO')
            
print(answer)