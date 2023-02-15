from collections import deque

def solution(n, computers):
    
    def BFS(i):
        q = deque()
        q.append(i)
        while(q):
            i = q.popleft()
            visit[i] = 1
            for a in range(n):
                if computers[i][a] == 1 and visit[a]==0: #edge는 있는데 방문한 적이 없는 경우
                        q.append(a)
                    
    
    visit = [0]*n
    count = 0
    for i in range(n):
        if visit[i]== 0:
            BFS(i)
            count+=1

    return count