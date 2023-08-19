N = 5 # 1 <= N <= 500 들어야하는 강의 수
inputs = [ # [들어야하는 강의 시간, 선수과목, -1]
    [10,-1],
    [10,1,-1],
    [4,1,-1],
    [4,3,1,-1],
    [3,3,-1]
]

from collections import deque

indegree = [0 for _ in range(N+1)] # 진입차수 관리
graph = [[] for _ in range(N+1)] # 과목 수 만큼 존재
q = deque()


for idx, input in enumerate(inputs):
    idx+=1
    cost,parents,tmp = input[0], input[1:-1], input[-1]

    for parent in parents:
        indegree[idx]+=1
        graph[parent].append([idx,cost])
    
    if indegree[idx] == 0:
        q.append((idx,cost))

print(graph)

result = 0 # 각 step별 최소 수강 시간
answer = [0 for _ in range(N+1)]
while q:
    
    for _ in range(len(q)):
        now,cost = q.popleft()
        answer[now] = max(answer[now],result+cost)
        for next,next_cost in graph[now]:
            indegree[next]-=1 # 간선 제거
            if indegree[next] == 0:
                q.append((next,next_cost))
                
    try:            
        result += max([value[1] for value in q]) # 각 단계별 최소 수강 시간
        print(q,result)
    except:
        print(q,result)

                
print(answer)