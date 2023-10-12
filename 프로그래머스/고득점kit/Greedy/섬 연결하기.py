def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    
    answer = 0
    for edge in costs:
        start, end, cost = edge
        a,b = find_parent(parent, start), find_parent(parent, end)
        if a == b:
            continue
        else:
            union_parent(parent, a,b)
            answer+=cost
        
    return answer