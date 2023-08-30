from collections import deque

for tc in range(int(input())):
    n = int(input())
    
    indegree = [0] * (n+1)
    
    graph = [[False]*(n+1) for i in range(n+1)]
    
    # 작년 순위 정보 입력
    data = list(map(int,input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] = True
            indegree[data[j]]+=1
            
    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a]+=1
            indegree[b]-=1
            
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a]-=1
            indegree[b]+=1
            
    # 위상 정렬 시작
    result = []
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    certain = True
    cycle = False
    
    for i in range(n):
        # 큐가 비어있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        
        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        result.append(now)
        
        for i in range(1,n+1):
            if graph[now][i]:
                indegree[i]-=1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)
    
    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()