from itertools import combinations

# N, M = 5, 3 # 2 <= N <= 50, 1 <= M <= 13
# chicken_map = [[0,0,1,0,0], [0,0,2,0,1], [0,1,2,0,0], [0,0,1,0,0], [0,0,0,0,2]]

# N, M = 5,2
# chicken_map = [[0,2,0,1,0], [1,0,1,0,0], [0,0,0,0,0], [2,0,0,1,1], [2,2,0,1,2]]

# N, M = 5,1
# chicken_map = [[1,2,0,0,0], [1,2,0,0,0], [1,2,0,0,0], [1,2,0,0,0], [1,2,0,0,0]]

# N, M = 5,1
# chicken_map = [[1,2,0,2,1], [1,2,0,2,1], [1,2,0,2,1], [1,2,0,2,1], [1,2,0,2,1]]

N, M = map(int,(input().split()))
chicken_map = []
for _ in range(N):
    chicken_map.append(list(map(int,input().split())))

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if chicken_map[i][j]==2:
            chickens.append([i,j])
        elif chicken_map[i][j]==1:
            houses.append([i,j])

candidates = list(combinations(chickens, M))

answers = []
for candidate in candidates:
    answer = 0
    for row2,column2 in houses:
        distance = N*N
        for row1,column1 in candidate:
            distance = min(distance, abs(row1-row2)+abs(column1-column2))
        answer+=distance
    answers.append(answer)
    
print(min(answers))