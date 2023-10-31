# N = 6
# K = 3
# apples = [
#     [3,4],
#     [2,5],
#     [5,3]
# ]

# L = 3
# change_directions = [
#     [3, 'D'],
#     [15,'L'],
#     [17,'D']
# ]

# N = 10 # N은 N*N 보드 크기. 2 <= N <= 100
# K = 4 #  사과의 개수
# apples = [[1,2], [1,3], [1,4], [1,5]] # k개 사과의 위치 [행,열]
# L = 4 # 뱀의 방향 변환 횟수. 1 <= L <= 100
# change_directions = [[8,'D'], [10,'D'], [11, 'D'], [13, 'L']] #[X,C] X는 게임 시작 후 X초 경과, C는 90도 회전방향 ('L' Left, 'D' Right)

# N = 10 # N은 N*N 보드 크기. 2 <= N <= 100
# K = 5 #  사과의 개수
# apples = [[1,5], [1,3], [1,2], [1,6], [1,7]] # k개 사과의 위치 [행,열]
# L = 4 # 뱀의 방향 변환 횟수. 1 <= L <= 100
# change_directions = [[8,'D'], [10,'D'], [11, 'D'], [13, 'L']] #[X,C] X는 게임 시작 후 X초 경과, C는 90도 회전방향 ('L' Left, 'D' Right)

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    apples.append(map(int,input().split()))
    
change_directions = []
L = int(input())
for _ in range(L):
    change_time, change_direction = input().split()
    change_directions.append([int(change_time), change_direction])
    

graph = [[0]*(N+1) for _ in range(N+1)]
for apple in apples:
    row, column = apple
    graph[row][column] = 1
    
from collections import deque
    
count=0
body = deque([])
head_row, head_column = 1,1 # 머리 시작점 (1행,1열)
# tail_row, tail_column = 1,1 # 꼬리 시작점 (1행,1열)
# body.append([tail_row, tail_column])
body.append([head_row, head_column])

graph[head_row][head_column] = 2 # 뱀의 시작 위치

directions = ['R','D','L','U']
direction = 0 # 처음 이동방향은 오른쪽
change_directions = deque(change_directions)
change_time, change_direction = change_directions.popleft()
while True:
    head_row, head_column = body[-1]
    tail_row, tail_column = body[0]
    
    if head_row < 1 or head_row > N or head_column < 1 or head_column > N: # 벽에 부딪히는 경우 종류
        break
    
    if direction == 0: # 오른쪽 진행
        if head_column + 1 > N: # 벽에 부딪히는 경우
            break
        else:
            head_column+=1
            if graph[head_row][head_column] == 2: # 자기 자신과 부딪히는 경우
                break
            if graph[head_row][head_column] == 1: # 사과가 있는 경우
                graph[head_row][head_column] = 2
                body.append([head_row, head_column])
            else: # 사과가 없는 경우
                graph[head_row][head_column] = 2
                graph[tail_row][tail_column] = 0
                body.append([head_row, head_column])
                body.popleft()
                
    elif direction == 1: # 아래쪽 진행
        if head_row + 1 > N: # 벽에 부딪히는 경우
            break
        else:
            head_row+=1
            if graph[head_row][head_column] == 2: # 자기 자신과 부딪히는 경우
                break
            if graph[head_row][head_column] == 1: # 사과가 있는 경우
                graph[head_row][head_column] = 2
                body.append([head_row, head_column])
            else: # 사과가 없는 경우
                graph[head_row][head_column] = 2
                graph[tail_row][tail_column] = 0
                body.append([head_row, head_column])
                body.popleft()
                
    elif direction == 2: # 왼쪽 진행
        if head_column - 1 < 1: # 벽에 부딪히는 경우
            break
        else:
            head_column -= 1
            if graph[head_row][head_column] == 2: # 자기 자신과 부딪히는 경우
                break
            if graph[head_row][head_column] == 1: # 사과가 있는 경우
                graph[head_row][head_column] = 2
                body.append([head_row, head_column])
            else: # 사과가 없는 경우
                graph[head_row][head_column] = 2
                graph[tail_row][tail_column] = 0
                body.append([head_row, head_column])
                body.popleft()
    
    elif direction == 3: # 위쪽 진행
        if head_row -1 < 1: # 벽에 부딪히는 경우
            break
        else:
            head_row -= 1
            if graph[head_row][head_column] == 2: # 자기 자신과 부딪히는 경우
                break
            if graph[head_row][head_column] == 1: # 사과가 있는 경우
                graph[head_row][head_column] = 2
                body.append([head_row, head_column])
            else: # 사과가 없는 경우
                graph[head_row][head_column] = 2
                graph[tail_row][tail_column] = 0
                body.append([head_row, head_column])
                body.popleft()
    
    count+=1
    if count == change_time:
        if change_direction == 'D': # 오른쪽으로 회전
            direction = (direction+1)%4
        elif change_direction == 'L': # 왼쪽으로 회전
            direction = (direction-1)%4
            
        if len(change_directions)!=0:
            change_time, change_direction = change_directions.popleft()
        

print(count+1) # 마지막 시간은 break문 때문에 증가하지 않기 때문