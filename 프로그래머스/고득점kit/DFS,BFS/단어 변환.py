from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        target_idx = words.index(target)
    
    begin = [begin]
    words = begin + words
    
    graph = [[]*len(words) for i in range(len(words))]
    
    INF = 1e9
    distances = [INF]*len(words)
    distances[0] = 0
    visited=[False]*len(words)

    for start, word1 in enumerate(words):
        for end, word2 in enumerate(words):
            count = sum([1 for i,j in zip(word1,word2) if i!=j])

            if count == 1:
                graph[start].append(end)
                graph[end].append(start)
                
    for row in graph:
        row = list(set(row))
    
    count = 0
    dq = deque([])
    for start in graph[0]:
        dq.append(start)
    
    while dq:
        count+=1
        for _ in range(len(dq)):
            now = dq.popleft()
            if visited[now] == True:
                continue
            else:
                visited[now] = True
            
            if distances[now] >= count:
                distances[now] = count
            
            for neighbor in graph[now]:
                dq.append(neighbor)
                                
    answer = distances[target_idx+1] # begin이 추가되면서 idx가 1씩 증가했기 때문
    return answer