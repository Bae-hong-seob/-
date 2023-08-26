N,M = 5,4 # 1 <= N,M <= 500 | N 은 여행지 도시 수(node) , M은 여행 계획에 속한 도시 수(방문할 node)
graph = [
    [0,1,0,1,1],
    [1,0,1,1,0],
    [0,1,0,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0]
]
trip_cities = [2,3,4,3] # 여행지는 1~N번까지의 번호로 구분

# solution : DFS -> stack. BFS -> q
start = trip_cities[0]
visited = [False for _ in range(N+1)]

stack = []
stack.append(start)
answers = []

while stack:
    now = stack.pop()
    if visited[now] == True:
        continue
    else: # 방문한 적이 없다면 방문 처리
        visited[now] = True
        answers.append(now)
    
    for neighbor, edge in enumerate(graph[now-1]): # 여행지는 1~N까지로 번호 설정
        neighbor+=1 # 여행지는 1~N까지로 번호 설정
        if edge == 1 and visited[neighbor] == False: # 연결되어있고 방문한 적이 없다면
            stack.append(neighbor)
            
print(answers)
answer = True
for trip_city in trip_cities:
    if trip_city in answers:
        continue
    else:
        answer = False
        
if answer == True:
    print('YES')
else:
    print('NO')