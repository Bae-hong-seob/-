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


# solution
def calculate_chicken_distance(houses, chickens):
    answers = []
    
    for house in houses:
        distances = []
        x_house, y_house = house
        for chicken in chickens:
            x_chicken, y_chicken = chicken
            distance = abs(x_house - x_chicken) + abs(y_house - y_chicken)
            distances.append(distance)
        answers.append(min(distances))
    
    return sum(answers)

from itertools import combinations
    
houses = []
chickens = []

for x_index, row in enumerate(chicken_map):
    for y_index, value in enumerate(row):
        if value == 1: # 집인 경우
            houses.append([x_index, y_index])
            
        elif value == 2: # 치킨집인 경우
            chickens.append([x_index, y_index])
            
        else:
            continue
        
candidates = list(combinations(chickens, M))

answer = []
for candidate in candidates:
    answer.append(calculate_chicken_distance(houses, candidate))
        
# print(houses)
# print(chickens)

# print(answer)
print(min(answer))