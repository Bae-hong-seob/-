# N = 6 # N은 N*N 보드 크기. 2 <= N <= 100
# K = 3 #  사과의 개수
# apples = [[3,4], [2,5], [5,3]] # k개 사과의 위치 [행,열]
# L = 3 # 뱀의 방향 변환 횟수. 1 <= L <= 100
# change_directions = [[3,'D'], [15,'L'], [17, 'D']] #[X,C] X는 게임 시작 후 X초 경과, C는 90도 회전방향 ('L' Left, 'D' Right)

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

K = int(input()) # 사과의 개수
apples = []
for _ in range(K):
    a,b = map(int,input().split())
    apples.append([a,b])

L = int(input())
change_directions = []
for _ in range(L):
    x,c = input().split()
    x,c = int(x), str(c)
    change_directions.append([x,c])

# solution
def move(now_direction, now_position):
	if now_direction == 0: # right
		now_position[1]+=1 # 열 증가
	elif now_direction == 1: #up
		now_position[0]-=1 # 행 감소
	elif now_direction == 2: # left
		now_position[1]-=1 # 열 감소
	elif now_direction == 3: #down
		now_position[0]+=1 # 행 증가
	else:
		return 'wrong direction !!!'
	
	return now_position
            

board = [[0]*N for _ in range(N)]
for apple in apples:
	row, column = apple
	board[row-1][column-1] = 1
# for row in board:
# 	print(row)
            
now_head_position, now_tail_positions, now_direction = [0,0],[],0
directions = [0, 1, 2, 3] # right, up, left, down

time = 0
while(True):
	if len(change_directions) != 0:
		if time == change_directions[0][0]: # 방향 회전할 시간
			X, C = change_directions.pop(0)
			
			if C == 'L': # 왼쪽으로 90도
				now_direction = directions[(now_direction+1) % 4]
			else: # 오른쪽으로 90도
				now_direction = directions[(now_direction-1) % 4]
	
	#print(now_head_position,now_direction)
	#print(now_tail_positions)
	time+=1
	
	past_head_position = [now_head_position[0], now_head_position[1]]
	now_head_position = move(now_direction, now_head_position)
	if type(now_head_position) == 'str':
		break
	
	if now_head_position[0] >= N or now_head_position[0] < 0 or now_head_position[1] >= N or now_head_position[1] < 0: # 벽과 부딪힌 경우
		break
	
	if now_head_position in now_tail_positions: # 자기 자신의 몸과 부딪힌 경우
		#print('block myself: ', now_head_position, now_tail_positions)
		break
	
	if board[now_head_position[0]][now_head_position[1]] == 1: # 사과가 있는 경우
		board[now_head_position[0]][now_head_position[1]] = 0
		now_tail_positions.append([past_head_position[0],past_head_position[1]])
	else: # 사과가 없는 경우
		now_tail_positions.append([past_head_position[0],past_head_position[1]])
		now_tail_positions = now_tail_positions[1:] # 꼬리도 이동

print(time)