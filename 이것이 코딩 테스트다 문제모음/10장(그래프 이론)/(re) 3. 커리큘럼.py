N = 5 # 1 <= N <= 500 들어야하는 강의 수
inputs = [ # [들어야하는 강의 시간, 선수과목, -1]
    [10,-1],
    [10,1,-1],
    [4,1,-1],
    [4,3,1,-1],
    [3,3,-1]
]

from collections import deque

indegrees = [0]*(N+1)
distances = [0]*(N+1)
graph = [[] for _ in range(N+1)]
q = deque([])

for idx, input in enumerate(inputs):
    idx+=1
    cost,parents,tmp = input[0], input[1:-1], input[-1]

    for parent in parents:
        indegrees[idx]+=1
        graph[parent].append([idx,cost])
    
    if indegrees[idx] == 0:
        q.append((idx,cost))

print(indegrees)
print(graph)

result = 0 # 각 step별 최소 수강 시간
answer = [0 for _ in range(N+1)]

while q:
    print(q, result)
    for i in range(len(q)):
        node, distance = q.popleft()
        answer[node] = max(answer[node], result+distance)
        for neighbor in graph[node]:
            neighbor_node, distance = neighbor
            indegrees[neighbor_node]-=1
            if indegrees[neighbor_node] == 0:
                q.append([neighbor_node, distance])
    try:
        result += max([value[1] for value in q]) # 각 단계별 최소 수강 시간
    except:
        result


print(answer)