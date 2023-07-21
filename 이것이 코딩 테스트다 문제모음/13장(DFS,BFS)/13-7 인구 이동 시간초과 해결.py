# N, L, R = 2, 20, 50 # 1 <= N <= 50 (N*N 크기), 1 <= L <= R <= 100 (L이상 R이하 인구수 차이)
# graph = [
#     [50, 30],
#     [20, 40]
# ]

# N,L,R = 2, 40,50
# graph = [
#     [50,30],
#     [20,40]
# ]

# N,L,R = 2, 20, 50
# graph = [
#     [50,30],
#     [30,40]
# ]

# N,L,R = 3, 5, 10
# graph = [
#     [10,15,20],
#     [20,30,25],
#     [40,22,10]
# ]

N,L,R = 4,10,50
graph = [
    [10,100,20,90],
    [80,100,60,70],
    [70,20,30,40],
    [50,20,100,10]
]

# N,L,R = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))

# 상,하,좌,우 탐색해서 방문노드 다 등록해놔야해. bfs. -> queue
from collections import deque

visited = [[False for _ in range(N)] for _ in range(N)]
start_points = [[row,column] for row in range(N) for column in range(N)]

move_row = [-1,0,1,0]
move_column = [0,-1,0,1]

def bfs(queue, number_of_area):
    sum_of_sub_graph = 0
    sub_graph = []
    
    while queue:
        row, column = queue.popleft()
        
        if visited[row][column]: # 전체 그래프에서 방문한 적이 있는 노드라면 패스 or 현재 그래프에서 방문한 적 있으면 패스
            continue
        
        else: # 첫 방문 노드라면
            visited[row][column] = True # 전체 그래프에서 현재 노드 방문 처리
            sum_of_sub_graph += graph[row][column]
            number_of_area+=1 # 연합 칸의 개수 증가
            sub_graph.append([row,column])
        
        if row >= 1: # 위쪽 방향 탐색
            if (L <= abs(graph[row][column] - graph[row-1][column]) <= R): # 연합 형성할 수 있는 경우
                queue.append([row-1, column]) # 방문 노드 추가
                
        if row <= N-2: # 아래쪽 방향 탐색
            if (L <= abs(graph[row][column] - graph[row+1][column]) <= R): # 연합 형성할 수 있는 경우
                queue.append([row+1, column]) # 방문 노드 추가
                
        if column >= 1: # 왼쪽 방향 탐색
            if (L <= abs(graph[row][column] - graph[row][column-1]) <= R): # 연합 형성할 수 있는 경우
                queue.append([row, column-1]) # 방문 노드 추가
        
        if column <= N-2: # 오른쪽 방향 탐색
            if (L <= abs(graph[row][column] - graph[row][column+1]) <= R): # 연합 형성할 수 있는 경우
                queue.append([row, column+1]) # 방문 노드 추가
    
    # graph 내에서 sub graph 형성.
    after_population = int(sum_of_sub_graph / number_of_area)
    
    for row,column in sub_graph:
        graph[row][column] = after_population
    
    return number_of_area

count = 0

new_graph = [row.copy() for row in graph]

while(True):
    original_graph = [row.copy() for row in new_graph]
    visited = [[False for _ in range(N)] for _ in range(N)] # update 된 그래프에서 다시 탐색
    number_of_graph = 0
    
    # 발생되는 sub graph마다 sum으로 normalize 해야함. 이건 start point가 달라지면서 graph가 계속 생성될꺼임
    
    for start_point in start_points: # 모든 점에 대하여 국경선 open 확인(=graph형성), 인구수 갱신
        row, column = start_point
        
        if not visited[row][column]: # 처음 방문하는 노드인 경우 sub graph 생성
            number_of_graph+=1
            queue = deque([start_point])
            number_of_area = 0
            number_of_area = bfs(queue, number_of_area) # new_graph는 인구수 갱신된 그래프.
    
    # check = sum([1 for row in range(N) for column in range(N) if original_graph[row][column] != new_graph[row][column]])
    # if check == 0: #두 그래프가 같다면 종료
    #     break
    
    if number_of_graph == N*N:
        break
    else:
        count+=1
        
print(count)