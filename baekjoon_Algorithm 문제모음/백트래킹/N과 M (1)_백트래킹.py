N,M = 3,1
N,M = 4,2
N,M = 4,4
#N,M = map(int, input().split())

answers = []
visited = [False]*(N+1)
def dfs(stack, visited):
    global N,M
    if len(stack)==M:
        answers.append(stack[:])
        return
    
    for next in range(1,N+1):
        if not visited[next]:
            visited[next]=True
            dfs(stack+[next],visited)
            visited[next]=False
            
dfs([],visited)
for answer in answers:
    for i in answer:
        print(i, end=' ')
    print()