N,M = 3,1
N,M = 4,2
N,M = 3,3
N,M = map(int, input().split())

def dfs(stack):
    if len(stack)==M:
        for i in stack:
            print(i, end=' ')
        print()
        return
        
    for next in range(1,N+1):
        dfs(stack+[next])

for i in range(1,N+1):
    dfs([i])