from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    m = int(input())
    now_year = []
    for _ in range(m):
        now_year.append(list(map(int,input().split())))

    edges = []
    for idx,up_team_idx in enumerate(last_year):
        for down_team_idx in last_year[idx+1:]:
            edges.append([up_team_idx, down_team_idx])


    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(n+1)]
    
    try:
        for start,end in edges:
            graph[start].append(end)
            indegree[end]+=1 # end로 들어오는 진입차수 1증가.


        for start,end in now_year:
            graph[end].remove(start)
            indegree[end]+=1
            graph[start].append(end)
            indegree[start]-=1


        result = [] # 알고리즘 수행 결과를 담을 리스트
        q = deque() # 큐 기능을 위한 deque 라이브러리 사용

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
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
            
            # 해당 원소와 연결된 노드에서 진입차수 1 빼기
            for j in graph[now]:
                indegree[j]-=1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

        if cycle:
            print('IMPOSSIBLE')
        elif not certain:
            print('?')
        else:
            for i in result:
                print(i, end=' ')
            print()

    except:
        print('IMPOSSIBLE')