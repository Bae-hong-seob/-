# N,M = 7,12 # 2 <= N <= 100000 집의 개수 | 1 <= M <= 1,000,000 길의 개수
# inputs = [ #[a번집, b번집, c 유지비]
#     [1,2,3],
#     [1,3,2],
#     [3,2,1],
#     [2,5,2],
#     [3,4,4],
#     [7,3,6],
#     [5,1,5],
#     [1,6,2],
#     [6,4,1],
#     [6,5,3],
#     [4,5,3],
#     [6,7,4]
# ]

N,M = map(int, input().split())
inputs = []
for _ in range(M):
    inputs.append(list(map(int, input().split())))
    

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N+1)]
inputs.sort(key = lambda x:x[2]) # cost 기준으로 정렬

costs = []
for input in inputs:
    a,b,cost = input
    if find_parent(parent,a) == find_parent(parent,b): #사이클 형성하는 경우
        continue
    else:
        union_parent(parent, a,b)
        costs.append(cost)

# print(costs)
print(sum(costs[:-1]))