def solution(x, y, n):
    if x==y:
        return 0
    
    INF = 1e9
    dp = [INF]*(y+1) #index가 곧 y를 의미
    
    stack = [x]
    for i in range(1,y):
        #print(i, stack)
        appends = set()
        while stack:
            now = stack.pop()
            if now == y:
                return dp[y]
            
            for next in [now+n, now*2, now*3]:
                if next <= y:
                    dp[next] = min(dp[next], i)
                    if next not in appends:
                        appends.add(next)       
        stack = appends

    return -1