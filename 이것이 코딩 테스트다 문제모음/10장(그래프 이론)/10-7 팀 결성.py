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

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(N+1)]

for input in inputs:
    calculate, a,b = input
    if calculate==0: #union
        union_parent(parent, a,b)
    else: # 같은 팀 여부 확인
        if find_parent(parent,a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')