# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
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
        
# 탑승구의 개수 입력받기
g = int(input())
# 비행기 개수 입력받기
p = int(input())

parent = [0]*(g+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g+1):
    parent[i] = i
    
result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구 루트 확인
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result+=1
    
print(result)