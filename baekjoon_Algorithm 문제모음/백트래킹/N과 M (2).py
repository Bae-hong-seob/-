N,M = 3,1
N,M = 4,2
N,M = 4,4
N,M = map(int, input().split())

numbers = [i for i in range(N+1)]
visited = [False]*(N+1)

def dfs(stack,visited):
    if len(stack)==M:
        for i in stack:
            print(i, end=' ')
        print()
        return
    now = stack[-1]
    for next in range(now+1,N+1):
        if visited[next]==False:
            visited[next]=True
            dfs(stack+[next],visited)
            visited[next]=False

for i in range(1,N+1): #시작점을 1부터 N까지 반복
    dfs([i],visited)