N = 4
graph = [
[0, 1, 2, 3],
[4, 0, 5, 6],
[7, 1, 0, 2],
[3, 4, 5, 0],
]

N=6
graph = [
[0, 1, 2, 3, 4, 5],
[1, 0, 2, 3, 4, 5],
[1, 2, 0, 3, 4, 5],
[1, 2, 3, 0, 4, 5],
[1, 2, 3, 4, 0, 5],
[1, 2, 3, 4, 5, 0],
]

N=8
graph=[
[0, 5, 4, 5, 4, 5, 4, 5],
[4, 0, 5, 1, 2, 3, 4, 5],
[9, 8, 0, 1, 2, 3, 1, 2],
[9, 9, 9, 0, 9, 9, 9, 9],
[1, 1, 1, 1, 0, 1, 1, 1],
[8, 7, 6, 5, 4, 0, 3, 2],
[9, 1, 9, 1, 9, 1, 0, 9],
[6, 5, 4, 3, 2, 1, 9, 0],
]

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

from itertools import combinations

min_value = int(1e9)  
def dfs(stack):
    global min_value
    if len(stack)==(N//2): #N은 최대 20. 즉 combinations은 10C2 = 10*9 / 2 = 45번개
        star, link = combinations(stack,2), combinations([i for i in range(1,N+1) if i not in stack],2)
        star_value, link_value = 0,0
        for i,j in star:
            star_value+=(graph[i-1][j-1]+graph[j-1][i-1])
        for i,j in link:
            link_value+=(graph[i-1][j-1]+graph[j-1][i-1])
        min_value = min(min_value, abs(star_value-link_value))
        return
    
    for next in range(stack[-1]+1, N+1):
        dfs(stack+[next])
        
dfs([1])
print(min_value)