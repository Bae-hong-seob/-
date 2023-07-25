# N = 4
# houses = [5,1,7,9]

N = int(input())
houses = list(map(int,input().split()))

candidates = set(houses)
#print(candidates)

answers = [[200000, 200000]] # distance, index

for candidate in candidates:
    total_distance = sum([abs(candidate - house) for house in houses])
    if total_distance < answers[0][0]: # 최솟값 변경
        answers = [] # answers 초기화.
        answers.append([total_distance, candidate])
        
    elif total_distance == answers[0][0]: # 후보군 추가
        answers.append([total_distance, candidate])        
        
answers = sorted(answers, key=lambda x : x[1])
print(answers[0][1])