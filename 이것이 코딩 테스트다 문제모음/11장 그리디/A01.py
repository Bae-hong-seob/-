n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹 수

count = 0 # 현재 그룹에 포함된 모험가 수

for i in data:
            count+=1
            if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
                        result+=1
                        count = 0                 
print(result)