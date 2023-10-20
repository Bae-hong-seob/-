from collections import deque

def solution(n, computers):
    count = 0
    visited = [False]*n
    for start in range(n):
        if visited[start] == False:
            dq = deque([start])
            count+=1

            while dq:
                now = dq.popleft()
                visited[now] = True
                for idx, computer in enumerate(computers[now]):
                    if computer == 1 and visited[idx] == False:
                        dq.append(idx)
        
        
    return count